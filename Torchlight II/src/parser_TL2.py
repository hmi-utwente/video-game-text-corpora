#!/usr/bin/python3
# Code by Judith van Stegeren
# 2020-05-12

import re
import json
import glob

# --------------------------
# For pretty printing
# --------------------------


def print_stats_old():
    with open("TL2_quests_and_unitnames.json") as infile:
      data = json.loads(infile.read())
    for t in [(x['dialog']['intro']['dialog'], x['dialog']['intro']['unit_displayname']) for x in data if x.get('dialog') and x['dialog'].get('intro') and x['dialog']['intro'].get('unit_displayname') and    x.get('reward')]:
      print(t)
      print()
    
    # the merryweather quest (=example in paper)  
    print([x for x in enumerate(data) if 'Merryweather' in json.dumps(x[1])]  )
    
def print_stats_new():
    # print all quest names:
    print("Total quests with names: {}".format(len([q.get('displayname') for q in quest_data if q.get('displayname')])))
    pprint.pprint([q.get('displayname') for q in quest_data if q.get('displayname')])
    
    # print all main quest names:
    print("Total quests in main questline: {}".format(len([q.get('displayname') for q in quest_data if q.get('displayname') and q.get('dialog') and q.get('dialog').get('moredetails')])))
    pprint.pprint([q.get('displayname') for q in quest_data if q.get('displayname') and q.get('dialog') and q.get('dialog').get('moredetails')])

def prettify(s):
    '''Remove newlines and
    the hex-codes (colournames) surrounding names in TL2 dialog strings
    The meaning of the codes can be found in /MEDIA/GLOBALS.DAT''' 
    s = re.sub("\\\\n","\n",s)
    s = re.sub("\\\\r","\n",s)
    s = re.sub("\n\n","\n",s)
    s = s.strip()
    s = re.sub(r"\|c[0-9ABCDEF][0-9ABCDEF][0-9ABCDEF][0-9ABCDEF][0-9ABCDEF][0-9ABCDEF][0-9ABCDEF][0-9ABCDEF](.*?)\|u",r"\1",s)
    s = re.sub(r"\|u","",s)
    return s
    
def print_line(units, line):
    '''Print one line of dialog from a parsed TL2 quest object
    line['unit_displayname'] is added to quest data by expand_quests_with_unit_names()
    units may be empty if we already know the displayname of units'''
    if line.get('unit_displayname'):
        print(line['unit_displayname'], end=": ")
    elif line.get('unitname'):
        print(unit_display_name(units, line['unitname']), end=": ")
    if line.get('dialogline'):
        print(prettify(line['dialogline']))
    if line.get('dialog_complete'):
        print(prettify(line['dialog_complete']))

def print_quest(units, quest):
    '''Pretty printing of parsed TL2 quest data'''
    if quest.get('displayname'):
        name = quest.get('displayname')
    else:
        name = quest.get('name')
    print(name)
    if 'dialog' in quest.keys():
        print("=" * len(quest['name']))
        for dialog_type in quest['dialog'].keys():
            print(dialog_type)
            print("-" * len(dialog_type))
            if type(quest['dialog'][dialog_type]) == list:
                for line in quest['dialog'][dialog_type]:
                    print_line(units, line)
            else:
                print_line(units, quest['dialog'][dialog_type])
            print()
        print()
        
# -----------------------------
# For parsing the game's files
# -----------------------------

def add_unit_name(units, line):
    '''Take a dialog line from a TL2 quest object and add the display name of the NPC
    that speaks that dialog line''' 
    if not line.get('unitname'):
        return
    matches = [unit for unit in units if unit.get('name') and unit.get('name').upper() == line['unitname']]
    if len(matches) > 0:
        displayname = matches[0]['displayname']
        filename = matches[0]['filename']
        line['unit_displayname'] = displayname
        line['unitfile'] = filename

def expand_quests_with_unit_names(units, quests):
    '''DEPRECATED
    
    Expand parsed quest objects with the displayname of NPCs that have 
    dialog lines. Use this function after you have parsed TL2's quests and units files'''
    for q_data in quests:
        if 'dialog' in q_data.keys():
            for dialog_type in q_data['dialog'].keys():
                if type(q_data['dialog'][dialog_type]) == list:
                    for line in q_data['dialog'][dialog_type]:
                        add_unit_name(units, line)
                else:
                    add_unit_name(units, q_data['dialog'][dialog_type])
    
def unit_display_name(units, unitid):
    '''DEPRECATED
    
    Matches a unit identifier from quest data to that unit's display name
    Quest data should be already parsed and sourced from /MEDIA/QUESTS
    Displayname is sourced from the unit-data in /MEDIA/UNITS/'''
    matches = [u for u in units if 'name' in u.keys() and u['name'].upper() == unitid]
    if len(matches) > 0:
        return matches[0]['displayname']
    else:
        return unitid
        
def expand_quest_with_unit_names(units, quest):
    '''Expand parsed quest objects with the displayname of NPCs that have 
    dialog lines. Use this function after you have parsed TL2's quests and units files'''
    if quest.get('dialog'):
        for dialog_type in quest.get('dialog').keys():
            dialogdata = quest.get('dialog').get(dialog_type)
            if type(dialogdata) == list:
                for line in dialogdata:
                    add_unit_name(units, line)
            else:
                add_unit_name(units, dialogdata)

def parse_angle_tags(s):
    '''Parse a line of Torchlight quest data of the format <TAG>KEY: VALUE'''
    if re.search(r'(\s*)(\[([A-Z0-9_]+)\])[\s\S]*?\1\[\/\3\]', s):
        raise ValueError("bracket tags found in text string: {}".format(s))
    if not re.search(r'<([A-Z0-9_]+)>', s):
        #print("{} does not contain angle brackets".format(s))
        return { 'text' : s }
    lines = s.split("\n")
    output = {}
    for line in lines:
        if line.strip() == "":
            continue
        #print(line)
        split_on_tag = re.split(r'<([A-Z0-9_ ]+)>', line.strip())
        #print(split_on_tag)
        split_on_key = re.split(r'([A-Z0-9_%]+):', split_on_tag[2])
        #print(split_on_key)
        #print("{} : {}".format(split_on_key[1], split_on_key[2]))
        if split_on_key[1].lower() == 'dialog':
            output['dialogline'] = split_on_key[2]
        else:
            output[split_on_key[1].lower()] = split_on_key[2]
    return output
    
def parse_structure(lines, depth):
    '''Parse one TL2 data file (i.e. the contents of /MEDIA/QUESTS/*.DAT or 
    /MEDIA/UNITS/*.DAT. This is a recursive function that is called by parse_quests and parse_units'''
    #lines = q.split("\n") # of geven we dit gewoon mee als argument: list ipv string? 
    output = {}
    parsed = []
    # find all strings
    for index, line in enumerate(lines):
        if depth == 0: # progress
            print("{}/{}".format(index, len(lines)))
        if line.strip() == "":
            continue
        if re.findall(r'^' + '\t' * depth + r'<', line):    # find the right scope (depth)
            output.update(parse_angle_tags(line))
            parsed.append(line)
        # find all start tags
        if re.findall(r'^' + '\t' * depth + r'\[([A-Z0-9_]+)\]', line):
            tag = re.findall(r'^' + '\t' * depth + r'\[([A-Z0-9_]+)\]', line)[0]
            startindex = index +1 # +1 to exclude the start tag
            currentindex = index +1
            # find corresponding end tag
            while not re.findall(r'^' + '\t' * depth + r'\[\/' + tag + r'\]', lines[currentindex]):
                currentindex += 1
            parsed = parsed + lines[startindex-1 : currentindex+1] # we do -1 and +1 to include the start and end tag
            children = parse_structure(lines[startindex : currentindex], depth+1)
            display_tag = tag.lower()
            print(display_tag)
            if display_tag not in output.keys(): # if it's new, save as key-value pair and we're done
                output[display_tag] = children
                continue
            elif type(output[display_tag]) != list: # if it's not a list yet, make it a list
                placeholder = output[display_tag]
                output[display_tag] = []
                output[display_tag].append(placeholder) # save it to the list of results
            output[display_tag].append(children)
    unparsed = [line for line in lines if line not in parsed]
    if len(unparsed) > 0:
        output['unparsed'] = [line for line in lines if line not in parsed]
    return output
    
def parse_quests(s):
    '''Parse TL2 quest data. Input s is a string that contains the contents of all files
    /MEDIA/QUESTS/*.DAT, separated by newlines.'''
    quests = [q + "[/QUEST]" for q in s.split("[/QUEST]\n") if q.strip() != ""]
    parsed_quests = []
    for q in quests:
        parsed_q = parse_structure(q.split("\n"),0)
        parsed_quests.append(parsed_q['quest'])
    return parsed_quests
    
#quest_files =  glob.glob("QUESTS/*.DAT") + glob.glob("QUESTS/*/*.DAT") + glob.glob("QUESTS/*/*/*.DAT")

quest_files = glob.glob("MEDIA/QUESTS/**/*.DAT", recursive=True)

def parse_quests_from_file(filelist_from_glob):
    '''Parse TL2 unit data from file. Input is a list of files in the QUESTS/ folder'''
    parsed_quests = []
    for questfile in filelist_from_glob:
        with open(questfile, "rb") as infile:
            quest_bytes = infile.read()
            quest_str = quest_bytes.decode('utf-16')
            parsed_q = parse_structure(quest_str.split("\n"),0)
            print(parsed_q)
            datapoint = parsed_q['quest']
            datapoint['filename'] = questfile
            parsed_quests.append(datapoint)
    return parsed_quests
            

def parse_units(s):
    '''Parse TL2 unit data. Input s is a string that contains the contents of all files
    /MEDIA/UNITS/*.DAT, separated by newlines.'''
    print(type(s))
    quests = [q + "[/UNIT]" for q in s.split("[/UNIT]\n") if q.strip() != ""]
    parsed_quests = []
    for q in quests:
        parsed_q = parse_structure(q.split("\n"),0)
        parsed_quests.append(parsed_q['unit'])
    return parsed_quests
    
#unit_files = glob.glob("UNITS/*.DAT") + glob.glob("UNITS/*/*.DAT") + glob.glob("UNITS/*/*/*.DAT")
unit_files = glob.glob("MEDIA/UNITS/**/*.DAT", recursive=True)

def parse_units_from_file(filelist_from_glob):
    '''Parse TL2 unit data from file. Input is a list of files in the UNITS/ folder'''
    parsed_units = []
    for unitfile in filelist_from_glob:
        with open(unitfile, "rb") as infile:
            unit_bytes = infile.read()
            unit_str = unit_bytes.decode('utf-16')
            parsed_unit = parse_structure(unit_str.split("\n"),0)
            print(parsed_unit)
            datapoint = parsed_unit['unit']
            datapoint['filename'] = unitfile
            parsed_units.append(datapoint)
    return parsed_units
    
def parse_from_file(filelist_from_glob, key_to_split_on):
    '''Parse TL2 unit data from file. Input is a list of files in the MEDIA/UNITS/ or MEDIA/QUESTS folder
    Generic function, works on all file types that follow TL2's XML format.
    
    input:
    filelist_from_glob -- result of glob.glob([pattern], recursive=True)
    key_to_split_on -- XML tag (lowercase) for type of file we want to parse. Examples: unit, quest'''
    parsed_units = []
    for unitfile in filelist_from_glob:
        with open(unitfile, "rb") as infile:
            unit_bytes = infile.read()
            unit_str = unit_bytes.decode('utf-16')
            parsed_unit = parse_structure(unit_str.split("\n"),0)
            print(parsed_unit)
            datapoint = parsed_unit[key_to_split_on]
            datapoint['filename'] = unitfile
            parsed_units.append(datapoint)
    return parsed_units
    
# --------------------------
# For creating the csv file
# --------------------------

def recurse(questobject):
    '''A simple way of recursing over all quest objects to print all lines'''
    global lines
    if type(questobject) == str:
        print(questobject)
        lines.append(prettify(questobject))
    if type(questobject) == dict:
        for k in questobject:
            if k in ['intro','passive','dialog','dialogline','complete','moredetails','return','huddetails','dialog_complete','details']:
                recurse(questobject[k])
    elif type(questobject) == list:
        for child in questobject:
            recurse(child)
            
def questobject_to_datapoint(dataset, questobject):
    if not questobject.get('name') and questobject.get('quest_guid'):
        raise ValueError("This is not a questobject! {}".format(questobject))
    if questobject.get('dialog'):
        dialog_to_datapoint(dataset, questobject, questobject.get('dialog'))

def dialog_to_datapoint(dataset, quest, dialog):
    keys = ['complete', 'intro', 'return', 'details', 'huddetails', 'passive', 'moredetails']
    for dialogtype in dialog.keys():
        if dialogtype not in keys:
            print(dialog)
            raise ValueError()
        if type(dialog[dialogtype]) == list:
            for child in dialog[dialogtype]:
                line_to_datapoint(dataset, quest, dialogtype, child)
        else:
            line_to_datapoint(dataset, quest, dialogtype, dialog[dialogtype])

def line_to_datapoint(dataset, quest, dialogtype, line):
    if not line.get('dialogline'):
        print("{}, {}, {}, {}".format(quest.get('filename'), quest.get('name'), dialogtype, line))
        print("Parser cannot parse this line to a datapoint!")
        return
    if line.get('dialogline'):
        datapoint = {}
        datapoint['text'] = prettify(line.get('dialogline'))
        datapoint['raw_text'] = line.get('dialogline')
        datapoint['dialogtype'] = dialogtype
        datapoint['questfile'] = quest.get('filename')
        datapoint['quest_name'] = quest.get('name')
        datapoint['quest_displayname'] = quest.get('displayname')
        
        # in the case of dialogue, we also have a speaker
        datapoint['speaker_unit'] = ""
        datapoint['speaker'] = ""
        datapoint['unitfile'] = ""
        if dialogtype not in ['huddetails', 'moredetails', 'details']:
            datapoint['speaker_unit'] = line.get('unitname')
            datapoint['speaker'] = line.get('unit_displayname')
            datapoint['unitfile'] = line.get('unitfile')
        dataset.append(datapoint)
        
    if line.get('dialog_complete'): # this record has an extra line of dialog!
        datapoint = {}
        datapoint['text'] = prettify(line.get('dialog_complete'))
        datapoint['raw_text'] = line.get('dialog_complete')
        datapoint['dialogtype'] = dialogtype + "_complete"
        datapoint['questfile'] = quest.get('filename')
        datapoint['quest_name'] = quest.get('name')
        datapoint['quest_displayname'] = quest.get('displayname')
        
        # in the case of dialogue, we also have a speaker
        datapoint['speaker_unit'] = ""
        datapoint['speaker'] = ""
        datapoint['unitfile'] = ""
        if dialogtype not in ['huddetails', 'moredetails', 'details']:
            datapoint['speaker_unit'] = line.get('unitname')
            datapoint['speaker'] = line.get('unit_displayname')
            datapoint['unitfile'] = line.get('unitfile')
        dataset.append(datapoint)
        
def main():
    quest_data = parse_from_file(quest_files, "quest")
    if len(quest_data) < 184:
        print("Something went wrong with parsing. Expected: 184. Parsed: {}".format(len(quest_data)))
        return quest_data
    unit_data = parse_from_file(unit_files, "unit")
    for quest in quest_data:
        expand_quest_with_unit_names(unit_data, quest)
    return quest_data, unit_data
