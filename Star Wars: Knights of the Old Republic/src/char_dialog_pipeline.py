#!/usr/bin/python2
#
# Python2 code for processing
# KOTOR1 game files for video game corpora project
#
# Judith van Stegeren, June 2020

import glob
import time
import re
import csv
import random
from pygff import gff32


# ----------------------------------
# Parsing GFF files
# ----------------------------------

def gff32_bulk_parse_status(pattern):
    '''find all gff-files by globpattern pattern
    and parse the gff-files with gff32 (python2 lib)
    Return a datastructure with filenames, 
    successes and failures, and the parsed contents of
    successfull files.'''
    
    gff_files = glob.glob(pattern)
    data = {}
    data['files'] = gff_files # all filesnames
    data['success'] = [] # filenames that were succesfully parsed
    data['failure'] = [] # filesnames that could not be parsed
    data['parsed'] = [] # parsed data from files from 'success'
    for gff in gff_files:
        with open(gff, "r") as infile:
            #print(gff)
            try:
                gff_contents = gff32.serialize.read_gff(infile)
                data['success'].append(gff)
                data['parsed'].append(gff_contents)
            except Exception as e:
                #print(type(e), e)
                data['failure'].append(gff)
                continue
    return data
    
def gff32_bulk_parse_dict(pattern):
    '''find all gff-files by globpattern pattern
    and parse the gff-files with gff32 (python2 lib)
    Return a dictionary where key = filename and 
    value = parsed contents of successfull files.'''
    
    gff_files = glob.glob(pattern)
    data = {}
    for gff in gff_files:
        fname = re.findall("../extracted/(.*)\.dlg", gff)[0]
        with open(gff, "r") as infile:
            try:
                #print(fname, gff)
                gff_contents = gff32.serialize.read_gff(infile)
                data[fname] = gff_contents
            except Exception as e:
                continue
    return data

# ---------------------------------
# Load the lookup dicts for
# strings, animations and
# character names
# ---------------------------------

def load_tlk(tlkfile):
    '''Load converted tlk-file as a lookup dictionary.
    tlkfile should be a txt-file from KOTOR1
    converted with tlk-txt-converter from NexusMods'''
    if tlkfile.endswith(".tlk"):
        raise ValueError("Error: please input a txt file.")
    sid2text = {}
    # load .tlk as txt
    # file was converted with tlk-txt-converter from NexusMods
    with open(tlkfile,"r") as infile:
      TLK = infile.read()

    for string in TLK.split("----------"):
        s = {}
        try:
            sid = int(string.split("String ")[1].split(":")[0])
            text = string.split("Text: ")[1].strip()
            sid2text[sid] = text
        except Exception as e:
            #print(string)
            pass
    return sid2text
    
def build_anim2text():
    '''Load dialoganimations.2da.csv from KOTOR1 and convert it to a dictionary
    
    Which file should you use?
    --------------------------
    You can find dialoganimations.2da in 2da.bif (use xoreos-tools unkeybif to extract file)
    convert the extracted file to csv with xoreos-tools (github) convert2da tool'''
    with open("../data/dialoganimations.2da.csv", "r") as infile:
        reader = csv.DictReader(infile)
        animations = { 10000+i : row['name'] for i, row in enumerate(reader) }
        return animations
    
    
def build_chid2text(sid2text):
    '''Build mapping from character_ids (in filename and TemplateResRef) to character name'''
    characterdata = gff32_bulk_parse_status("../extracted/*.utc")
    return { c['TemplateResRef'] : char2name(sid2text, c) for c in characterdata['parsed'] }

def char2conv(char):
    '''Given a character data structure, return the corresponding parsed dlg'''
    if char['Conversation'] == '':
        return None
    dlgfile = "../extracted/" + char['Conversation'] + ".dlg"
    with open(dlgfile, "r") as infile:
        dlg = gff32.serialize.read_gff(infile)
        return dlg
    
def dlg2start(dlg):
    '''Given a dlg data structure, return the list of dialogue acts that 
    are a conversation root node in the dlg'''
    return [dlg['EntryList'][startindex] for startindex in [sl['Index'] for sl in dlg['StartingList']]]


# -------------------------------------
# Pretty printing of names,
# dialogue acts (da) (= 1 conversation turn)
# and dialogue trees
# -------------------------------------

def char2name(sid2text, c):
    '''Return the name of a character'''
    if c['LastName'][0] == -1:
        return sid2text[c['FirstName'][0]]
    return " ".join([sid2text[c['FirstName'][0]], sid2text[c['LastName'][0]]])

def da2text(sid2text, da):
    '''Turn the text from a dialogue act into 
    a human readable string. 
    Just the dialog lines, no speaker info'''
    index = da['Text'][0]
    if index != -1:
        return re.sub(r"[\n\r]+"," ",sid2text[da['Text'][0]])
    return ''

def pretty_print_da(sid2text, da, conversation_owner, chid2text, anim2text):
    '''Turn a dialogue act into a prettified human-readable string
    (speaker) [to (listener)] [(emotion)]: (dialogue line)'''
    line = ""
    # speaker
    if 'Speaker' not in da.keys():
        speaker = "Player"
    elif da['Speaker'] == '':
        if conversation_owner == '':
            speaker = "Conversation owner" # placeholder
        else:
            speaker = conversation_owner
    else:
        speaker = chid2text.get(da["Speaker"])
        if not speaker:
            speaker = da["Speaker"]
    line += "{}".format(speaker)
    # listener
    if 'Listener' in da.keys() and da['Listener'] != "":
        listener = chid2text.get(da['Listener'])
        if not listener:
            listener = da['Listener']
        line += " to {}".format(listener)
    line += ": "
    line += da2text(sid2text, da)
    # animation
    animlist = list(da['AnimList'])
    if animlist != []:
        for anim_struct in animlist:
            animation = anim2text.get(anim_struct['Animation'])
            if not animation:
                continue
            participant = chid2text.get(anim_struct['Participant'])
            if not participant:
                participant = anim_struct['Participant']
            if participant == "OWNER":
                participant = conversation_owner
            elif participant == "PLAYER":
                participant = 'Player'
            line += "\n[Animation {}: {}]".format(participant, animation)
    # comment    
    if da['Comment'] != '':
        commenttext = da['Comment'].strip()
        commenttext = re.sub("//","",commenttext)
        commenttext = re.sub(r"[\n\r]+"," ",commenttext)
        line += "\n[{}]".format(commenttext)
    return line
    
    
def pretty_print_dlg(sid2text, dlg, conversation_owner, chid2text, anim2text, quiet):
    '''Pretty print an entire dlg file in script form'''
    log =  { 'npc' : [], 'pc' : [] } # outside loop, so we don't print everything len(dlg2start(dlg)) times
    for startingpoint in dlg2start(dlg):
        print_tree(dlg, sid2text, startingpoint, 0, log, conversation_owner, chid2text, anim2text, quiet)
        print("")
        #print("Printed pc lines: {}, printed npc lines: {}".format(len(log['pc']), len(log['npc'])))

    
def print_tree(dlg, sid2text, dialogue_act, depth, processed, conversation_owner, chid2text, anim2text, quiet=False):
    '''Parse and print all dialogue trees present in dlg.
    
    dlg -- the dlg datastructure 
    sid2text -- mapping from game string ids to python strings
    dialogue_act -- the dialogue act we are currently processing
    depth -- the recursion depth
    processed -- references to dialogue acts we have already printed
                 in the form of a dictionary which must contain 
                 'npc' and 'pc' keys (as list)
    conversation_owner --   if an NPC talks and Speaker property is Empty, 
                            the speaker is  the conversation owner (obtain this info 
                            from .utc file that refers to this particular dlg
    chid2text -- character id to text
    anim2text -- mapping from animation ids to human readable string
    quiet -- when True, supresses printing

    note:
    dlg['EntryList']: contains NPC dialogue structs (=dialog acts)
    dlg['ReplyList']: contains Player dialogue structs (=dialog acts)
    '''
    if processed['pc'] == []: # if we call this function for the first time, 'blacklist' all root nodes
        processed['pc'] = [startingpoint['Index'] for startingpoint in dlg['StartingList']]
    if True or da2text(sid2text, dialogue_act) != "":  # only print lines with content
        #print(depth * ">" + pretty_print_da(sid2text, dialogue_act))
        if not quiet:
            print(pretty_print_da(sid2text, dialogue_act, conversation_owner, chid2text, anim2text))
        depth += 1
    if 'RepliesList' in dialogue_act.keys(): # NPC is talking now
        for reply in dialogue_act['RepliesList']:
            index = reply['Index']
            if index not in processed['npc']:
                processed['npc'].append(index)
                print_tree(dlg, sid2text, dlg['ReplyList'][index], depth, processed, conversation_owner, chid2text, anim2text, quiet)
            else:
                if not quiet:
                    print("Already printed subtree: {}...".format(da2text(sid2text, dlg['ReplyList'][index])[:50]))
                pass
    elif 'EntriesList' in dialogue_act.keys(): # NPC is talking
        for reply in dialogue_act['EntriesList']:
            index = reply['Index']
            if index not in processed['pc']:
                processed['pc'].append(index)
                print_tree(dlg, sid2text, dlg['EntryList'][index], depth, processed, conversation_owner, chid2text, anim2text, quiet)
            else:
                if not quiet:
                    print("Already printed subtree: {}...".format(da2text(sid2text, dlg['EntryList'][index])[:50]))
                pass

# ------------------------------
# Code for building a 2d
# dataset (csv) from the parsed
# game files
# -----------------------------

def da2datapoint(sid2text, da, dlg_name, conversation_owner, chid2text, anim2text):
    '''Turn a dialogue act into a datapoint for the dataset,
    similar to the prettified string from pretty_print_da;
    
    datapoint must contain the following keys:
    speaker
    listener
    emotion
    text (=dialogue line)
    comment
    previous
    next
    audiofile
    '''
    datapoint = {}
    # speaker
    if 'Speaker' not in da.keys():
        speaker = "Player"
    elif da['Speaker'] == '':
        if conversation_owner == '':
            speaker = "Conversation owner" # placeholder
        else:
            speaker = conversation_owner
    else:
        speaker = chid2text.get(da["Speaker"])
        if not speaker:
            speaker = da["Speaker"]
    datapoint['speaker'] = speaker
    # listener
    listener = ''
    if 'Listener' in da.keys() and da['Listener'] != "":
        listener = chid2text.get(da['Listener'])
        if not listener:
            listener = da['Listener']
    datapoint['listener'] = listener
    # dialog line
    datapoint['text'] = da2text(sid2text, da)
    # animation
    datapoint['animation'] = []
    animlist = list(da['AnimList'])
    if animlist != []:
        for anim_struct in animlist:
            animation = anim2text.get(anim_struct['Animation'])
            if not animation:
                continue
            participant = chid2text.get(anim_struct['Participant'])
            if not participant:
                participant = anim_struct['Participant']
            if participant == "OWNER":
                participant = conversation_owner
            elif participant == "PLAYER":
                participant = 'Player'
            datapoint['animation'].append({participant : animation})
    # comment
    commenttext = ''
    if da['Comment'] != '':
        commenttext = da['Comment'].strip()
        commenttext = re.sub("//","",commenttext)
        commenttext = re.sub(r"[\n\r]+"," ",commenttext)
    datapoint['comment'] = commenttext
    datapoint['previous'] = []
    datapoint['next'] = []
    datapoint['source_dlg'] = dlg_name
    # audiofile
    # for testing:
    #datapoint['sound_exists'] = da.get('SoundExists')
    #datapoint['sound'] = da.get('Sound')
    #datapoint['vo_resref'] = da.get("VO_ResRef")
    datapoint['audiofile'] = ''
    if da.get('SoundExists') == 1:
        if da.get('Sound'):
            datapoint['audiofile'] = da.get('Sound').upper() + ".mp3"
        else:
            datapoint['audiofile'] = da.get('VO_ResRef').upper() + ".mp3"
    #datapoint['Speechtype'] = ''
    #if da.get('SoundExists') and da.get('SoundExists') == 1:
    #    datapoint['speechtype'] = 'human'
    #elif da.get('SoundExists') and da.get('SoundExists') == 3:
    #    datapoint['alien'] = 
    #datapoint['audiofile'] = ""
    #if da.get('SoundExists') and da.get('SoundExists') > 0 and da.get('VO_ResRef') != "":
    #    datapoint['audiofile'] = da.get('Sound').upper() + ".mp3"        
    return datapoint

def dp_in_dataset(dataset, datapoint):
    return [dp for dp in dataset if dataset[dp]['source_dlg'] == datapoint['source_dlg'] and 
                                    dataset[dp]['text'] == datapoint['text'] and 
                                    dataset[dp]['speaker'] == datapoint['speaker'] and 
                                    dataset[dp]['listener'] == datapoint['listener']] != []

def dp2index(dataset, datapoint):
    return [dp for dp in dataset if dataset[dp]['source_dlg'] == datapoint['source_dlg'] and 
                                dataset[dp]['text'] == datapoint['text'] and 
                               dataset[dp]['speaker'] == datapoint['speaker'] and 
                               dataset[dp]['listener'] == datapoint['listener']]
    
def tree2dataset(dataset, dlg, dlg_name, sid2text, dialogue_act, previous, conversation_owner, chid2text, anim2text):
    '''Recursively parse dialog (sub)trees to turn its dialogue acts into datapoints
    Save datapoints to dataset
    
    Clean recursion!'''
    datapoint = da2datapoint(sid2text, dialogue_act, dlg_name, conversation_owner, chid2text, anim2text)
    datapoint['previous'] = [previous]
    # if text is empty, don't do anything with current datapoint, but process children
    if datapoint['text'] == '':
        if 'RepliesList' in dialogue_act.keys(): # NPC is talking now
            for reply in dialogue_act['RepliesList']:
                index = reply['Index']
                tree2dataset(dataset, dlg, dlg_name, sid2text, dlg['ReplyList'][index], previous, conversation_owner, chid2text, anim2text)
        elif 'EntriesList' in dialogue_act.keys(): # NPC is talking
            for reply in dialogue_act['EntriesList']:
                index = reply['Index']
                tree2dataset(dataset, dlg, dlg_name, sid2text, dlg['EntryList'][index], previous, conversation_owner, chid2text, anim2text)
        return
    # if text is non-empty and text is not yet part of dataset
    index = dp2index(dataset, datapoint)
    if index == []: # if this is not yet part of the dataset
        # create a unique id
        if len(dataset) != 0:
            i = max(dataset.keys())+1
        else:
            i = 0
        # add to dataset
        dataset[i] = datapoint
        # process children
        if 'RepliesList' in dialogue_act.keys(): # NPC is talking now
            for reply in dialogue_act['RepliesList']:
                index = reply['Index']
                tree2dataset(dataset, dlg, dlg_name, sid2text, dlg['ReplyList'][index], i, conversation_owner, chid2text, anim2text)
        elif 'EntriesList' in dialogue_act.keys(): # NPC is talking
            for reply in dialogue_act['EntriesList']:
                index = reply['Index']
                tree2dataset(dataset, dlg, dlg_name, sid2text, dlg['EntryList'][index], i, conversation_owner, chid2text, anim2text)
    else: #only do this for non-empty strings
        if previous:
            if len(index) > 1:
                print("Strange! multiple indices for datapoint.")
                print("datapoint: {}".format(datapoint))
                print(index)
            else:
                index = index[0]
            if previous not in dataset[index]['previous']:
                dataset[index]['previous'].append(previous)

def dlg2dataset(dataset, sid2text, dlg, dlg_name, conversation_owner, chid2text, anim2text):
    '''Parse and convert an entire dlg file to datapoints'''
    for startingpoint in dlg2start(dlg):
        tree2dataset(dataset, dlg, dlg_name, sid2text, startingpoint, None, conversation_owner, chid2text, anim2text)  
   
def create_dataset():
    '''Load all datafiles, parse the full trees and convert this to a 'flat' 2D dataset.
    Because of the recursion and all deduplication checks, this takes about 6 mins to run.
    Writes the dataset to dataset.csv and returns the dataset.
    
    It requires a folder ../extracted/ with extracted .utc and dlg files from
    Star Wars: Knights of the Old Republic.
    '''
    sid2text = load_tlk("../data/TLK-Txt.txt")
    chid2text = build_chid2text(sid2text)
    anim2text = build_anim2text()
    characterdata = gff32_bulk_parse_status("../extracted/*.utc")
    print("Loaded {} character files".format(len(characterdata['success'])))
    characters_with_dialog = [char for char in characterdata['parsed'] if char['Conversation'] != '']

    dataset = {}
    # character-owned dialog
    log = []
    for char in characters_with_dialog:
        log.append(char['Conversation'])
        print("Adding {} to dataset...".format(char['Conversation']))
        dlg2dataset(dataset, sid2text, char2conv(char), char['Conversation'], char2name(sid2text, char), chid2text, anim2text)
    
    # orphaned dialog
    dialogdata = gff32_bulk_parse_dict("../extracted/*.dlg") # function that returns a dictionary filename -> data
    orphaned_dialogs = { fname : dialogdata[fname] for fname in dialogdata if fname not in log }
    print("{}/{} dialogs without conversation owner".format(len(orphaned_dialogs), len(dialogdata)))
    for dlg_name in orphaned_dialogs:
        log.append(dlg_name)
        print("Adding {} to dataset...".format(dlg_name))
        dlg2dataset(dataset, sid2text, orphaned_dialogs[dlg_name], dlg_name, '', chid2text, anim2text)
        
    # postprocessing: fill 'next' field:
    n = len(dataset)
    for dp in dataset:
        print("{}/{}".format(dp, n))
        dataset[dp]['next'] = [i for i in dataset if dp in dataset[i]['previous']]
        
    # write to csv file
    datestr = datetime.datetime.now().date().strftime("%Y%m%d")
    with open("../data/dataset_" + datestr + ".csv","w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['id','speaker','listener','text','animation','comment','next','previous','source_dlg','audiofile'])
        writer.writeheader()
        for key_id in dataset:
            print(dataset[key_id])
            custom_datapoint = {}
            custom_datapoint["id"] = key_id
            custom_datapoint.update(dataset[key_id])
            print(custom_datapoint)
            writer.writerow(custom_datapoint)

    return dataset
    
def explore_dataset(dataset):
    # processed dlg files
    print("DLG source files: {}".format(len(set([dataset[dp]['source_dlg'] for dp in dataset]))))
    # unique lines
    print("Unique lines: {}".format(len(set([dataset[dp]['text'] for dp in dataset]))))
    # unique NPCs
    print("Unique NPCs: {}".format(len(set([dataset[dp]['speaker'] for dp in dataset] + [dataset[dp]['listener'] for dp in dataset]))))
    # starting points/root nodes:
    print("Root nodes: {}".format(len([dp for dp in dataset if None in dataset[dp]['previous']])))
    print("End nodes: {}".format(len([dp for dp in dataset if dataset[dp]['next'] == []])))
    # animations
    print("Dialog lines with animations: {}".format(len([dp for dp in dataset if dataset[dp]['animation'] != []])))
    print("Dialog lines with multiple animations: {}".format(len([dp for dp in dataset if len(dataset[dp]['animation']) > 1])))
    # print latex for example dialogue act
    data = dataset
    for key in data['28209'].keys():
        print(re.sub("[\[\]\{\}]","",re.sub("_","\\_","{} & {} \\\\".format(key.capitalize(),data['28209'][key]))))
    # print mandalorian raiders bit as latex
    for key in list(data.keys()):
        if type(key) != int:
            data[int(key)] = data[key]
            data.pop(key)

    start = 28181
    while data[start]['next'] != []:
        s = "{} & {} & {} & {}".format(start, data[start]['speaker'], data[start]['text'], data[start]['animation'])
        s = re.sub("[\[\]\{\}]", "", s)
        s = re.sub("_", "\\_", s)
        print(s)
        start = random.choice(data[start]['next'])

    s = "{} & {} & {} & {}".format(start, data[start]['speaker'], data[start]['text'], data[start]['animation'])
    s = re.sub("[\[\]\{\}]", "", s)
    s = re.sub("_", "\\_", s)
    print(s)
    # print all possible animations present in data
    anims = set([b for x in data for a in data[x]['animation'] for b in a.values()])
    for anim in anims:
        print("{}: {}".format(anim, len([x for x in data for a in data[x]['animation'] if anim in a.values()]))) # might not work

def print_random_subtree(dataset):
    startingpoints = [dp for dp in dataset if None in dataset[dp]['previous']]
    r = random.choice(startingpoints)    
    while dataset[r]['next'] == []:
        r = random.choice(startingpoints)
    while dataset[r]['next'] != []:
        print("{}: {}".format(dataset[r]['speaker'], dataset[r]['text']))
        r = random.choice(dataset[r]['next'])

def main():
    dataset = create_dataset()
    explore_dataset(dataset)
