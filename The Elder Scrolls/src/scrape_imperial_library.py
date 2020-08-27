#!/usr/bin/python
import datetime
import json
import pickle
import re
import urllib.request
from bs4 import BeautifulSoup

def create_catalogue():
    hostname = "https://www.imperial-library.info"
    
    morrowind = "https://www.imperial-library.info/books/tes3%3Amorrowind/by-title"
    oblivion = "https://www.imperial-library.info/books/tes4%3Aoblivion/by-title"
    skyrim = "https://www.imperial-library.info/books/tes5%3Askyrim/by-title"
    tesonline = "https://www.imperial-library.info/books/tes%3Aonline/by-title"
    arena = "https://www.imperial-library.info/books/tes1%3Aarena/by-title"
    daggerfall = "https://www.imperial-library.info/books/tes2%3Adaggerfall/by-title"
    
    library = {}
    # scrape the list of books for all games in the list
    for game_url, game_name in [(morrowind, "Morrowind"), (oblivion, "Oblivion"), (skyrim, "Skyrim"), (tesonline, "TES: Online"), (arena, "Arena"), (daggerfall, "Daggerfall")]:
        print(game_name)
        game_booklist_page = urllib.request.urlopen(game_url)
        html = game_booklist_page.read().decode('utf-8') # because charset=utf-8 in header of result
        soup = BeautifulSoup(html, 'html.parser')

        rows = soup.select('.views-row')
        for r in rows:
            bookurl = r.find("a").attrs['href']
            if bookurl.startswith("/content") or bookurl.startswith("/node"):
                bookurl = hostname + bookurl
            bookurl = re.sub("info//","info/",bookurl)
            print(bookurl)
            if bookurl in library:
                library[bookurl]['game'].append(game_name)
                print("Book {} by {} appears in game {}".format(book['title'], book['author'], game_name))
            else:
                book = {}
                book['game'] = [game_name]
                book['url'] = bookurl
                book['description'] = ""
                try:    
                    book['author'] = r.select('.views-field-field-author-value')[0].text.strip()
                    book['title'] = r.find("a").text
                except Exception as e:
                    continue
                try:
                    book['description'] = r.select('.views-field-field-summary-value')[0].text.strip()
                except Exception as e:
                    print("Can't find a description for", book['title'])
                library[bookurl] = book
                print("{} by {}".format(book['title'], book['author']))
    print("After processing game lists: {} unique book in catalogue".format(len(library.keys())))
    return library

def image_book(book):
    result = urllib.request.urlopen(book['url'])
    data = result.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    if soup.find(class_="book-navigation") and not book.get('series'):
        return
    else:
        prose = soup.find(id="main").find(class_="prose")
        alts = "\n".join([img.attrs['alt'] for img in prose.findAll('img')])
        return alts

def scrape_and_expand(library):
    hostname = "https://www.imperial-library.info"
    print("Before scraping and expanding: {} unique book in catalogue".format(len(library.keys())))
    # scrape the texts for all books in our library
    # expand series to books
    new_book_urls = []
    total_removed = 0
    updates = 0
    for book in list(library.values()):
        if book.get('text'):
            continue
        result = urllib.request.urlopen(book['url'])
        data = result.read().decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')
        # some books have multiple volumes
        # in that case, there is a menu at the bottom of the page that lists all volumes
        # currently, we're not using the volumes
        if soup.find(class_="book-navigation") and not book.get('series'):
            print(book['title'], "consists of multiple volumes!")
            children = [(x.text, x.attrs['href']) for x in soup.find(class_='book-navigation').findAll("a")]
            for child in children:
                if child[0] == 'up':
                    continue
                bookurl = child[1]
                if bookurl.startswith("/content") or bookurl.startswith("/node"):
                    bookurl = hostname + bookurl
                bookurl = re.sub("info//","info/",bookurl)
                if bookurl not in library:
                    child_book = {}
                    child_book['series'] = book['title']
                    child_book['game'] = book['game']
                    child_book['url'] = bookurl
                    child_book['author'] = book['author']
                    child_book['title'] = child[0]
                    child_book['description'] = book['description']
                    library[bookurl] = child_book
                    updates += 1
                    print("{} by {}".format(child_book['title'], child_book['author']))
                    new_book_urls.append(bookurl)
            print("Removing series {}".format(book['title']))
            total_removed += 1
            updated += 1
            library.pop(book['url'])
            continue
        else:
            prose = soup.find(id="main").find(class_="prose")
            book['text'] = "\n".join([unit.text.strip() for unit in prose.findAll(["p","h1","h2","h3"]) if not unit.findParent(class_=["field-field-comment","field-field-author"])]) # concat all paragraphs and titles that are not author names and librarian comments
            # some books have webpages where the text does not have <p> tags. Then we will also consider the text in divs. 
            if len(book['text']) < 10:
                book['text'] = "\n".join([unit.text.strip() for unit in prose.findAll(["p","h1","h2","h3","div"]) if not "field-field-author" in unit.get_attribute_list("class") and not "field-field-comment" in unit.get_attribute_list("class") and not unit.findParent(class_=["field-field-comment","field-field-author"])])
            # if the book still has no text, it consists only of images:
            if len(book['text']) < 10:
                book['text'] = image_book(book)
            # if the book still has no text, check the librarian comments
            if len(book['text']) < 10:
                comment = "\n".join([unit.text.strip() for unit in prose.findAll(["p","h1","h2","h3","div"],class_="field-field-comment")])
                comment = comment.replace("Librarian Comment:\xa0\n","")
                if "Book added by" not in comment:
                    book['text'] = comment
            if len(book['text']) > 0:
                updates += 1
                print(book['text'][:50])
    print("After expanding series and scraping: {} unique books in catalogue".format(len(library.keys())))
    print("{} total series removed from catalogue".format(total_removed))
    print("{} modifications of catalogue".format(updates))
    return library, new_book_urls, total_removed, updates
    
def main():
    library = create_catalogue()
    library, new_book_urls, total_removed, updates = scrape_and_expand(library)
    datestr = datetime.datetime.now().date().strftime("%Y%m%d")
    with open("imperial_library_" + datestr + ".pickle","w") as outfile:
        pickle.dump(library, outfile, pickle.HIGHEST_PROTOCOL)
    with open("imperial_library_" + datestr + '.json',"w") as outfile:
        outfile.write(json.dumps(library))
