# game-corpora-torchlight2
Video game corpus (text dataset) of quests, units and dialog lines from RPG game TorchLight 2 by Runic Games. 

## Files
### src/
Contains the python3 code with which I extracted the data from the original gamefiles. 
It also includes some utility functions for pretty printing. The code has no special prerequisites. 

```
$ python
>>> import parser_TL2
>>> quests = parser_TL2.main()
>>> len(quests)
184
>>> parser_TL2.print_quest([], quests[100])
Bring Out Your Dead
===================
details
-------
Convince the Estherian Spirits to let you into the Bone Gallery, and retrieve the Rosamortis.
Bring the Rosamortis to Selrenki, in Skull Hollow in the Temple Steppes.

complete
--------
Shady Character: You found it?  Fantastic!  Here, let me just pay you for your trouble, and I'll be on my way ...

return
------
Shady Character: The Rosamortis is apparently a handy little thingamajig that can save the life of someone who's 
been mortally wounded.  Obviously, this sort of thing would be very valuable to someone whose homeland were 
being invaded by, for example, bear-people ... But, as much as the Rosamortis is worth, it doesn't do me any 
good if I can't get inside the Sepulcher of Sorrows to retrieve it!\n\nThe Vanquishers' commander told me 
about this thing, like I could just stroll out here and pick it up.  But she didn't tell me the gate was locked 
with chains only a ghost can open!  And, of course, while I wasted precious time trying to find another way in, 
the Sturmbeorn showed up and cut off my way out.

intro
-----
Shady Character: I got a proposition for you ... a little "I scratch my back, you scratch yours" kind of thing.
See this crypt over here?  It's called the Bone Gallery, and there's a little thing in there called the 
Rosamortis ... which, while pretty valuable, is also guarded by the biggest undead monstrosity I've ever 
seen!\n\nYou'll have to convince the Estherian spirits to unlock the Ghost Chains and give you access, then 
get the Rosamortis away from that monster ... but I promise to make it worth your while!\n

huddetails
----------
- Rouse the Estherian Spirits, and enter the Bone Gallery in the Temple Steppes.  Retrieve the Rosamortis
- Bring the Rosamortis back to Selrenki in Skull Hollow, in the Temple Steppes
```

### data/
quests.txt and units.txt are concatenations of all .dat files from the MEDIA/QUESTS/ and MEDIA/UNITS/ folders. 
These are unparsed original datafiles. 
TL2_quests.json contains the parsed and cleaned data mentioned in the paper (to be published). 

## Questions?
Feel free to email me if you have any questions about the code. 
I'd love to hear from you if you use this dataset in research. 
