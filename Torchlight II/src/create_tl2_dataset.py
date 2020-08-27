# script for creating dataset for TL from scratch
import glob
import parser_TL2

quest_data, unit_data = parser_TL2.main()

if len(quest_data) != 184:
    raise ValueError("Not all quests have been parsed properly. Expected: 184. Result: {}".format(len(quest_data)))

parser_TL2.lines = []
parser_TL2.recurse(quest_data)

dataset_csv = []
for questobject in quest_data:
    parser_TL2.questobject_to_datapoint(dataset_csv, questobject)

if len([line for line in parser_TL2.lines if line not in [d.get('text') for d in dataset_csv]]) > 0:
    raise ValueError("Not all lines from source files have been added to dataset.")

import csv

outfile = open("dataset_TL2.csv","w")
writer = csv.DictWriter(outfile, fieldnames=['speaker','text','dialogtype','quest_displayname','quest_name','questfile','speaker_unit','unitfile','raw_text'])
writer.writeheader()
for datapoint in dataset_csv:
    writer.writerow(datapoint)
