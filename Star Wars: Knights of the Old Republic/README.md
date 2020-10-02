# Star Wars: Knights of the Old Republic 
Video game corpus (text dataset) of dialog lines from RPG game Star Wars: Knights of the Old Republic by BioWare and LucasArts.

## About the game
Star Wars: Knights of the Old Republic (2003) is an RPG by LucasArts and BioWare. 
Although it’s a few decades old, it’s still popular because of the high-quality writing and voice-acting. 
The game is special because the story works with branching dialogue: during conversations with NPCs, the player can choose how to react.

The player character can choose to help someone or ignore them, tell the truth or lie, befriend someone or kill them. 
Choices have consequences for the game’s story. The player’s (moral) alignment, ranging from good/jedi to evil/sith, is a result of all these micro-choices, and you get a storyline and in-game force powers according to your alignment.

To see all the different dialogue options and all possible conversations, story lines and endings, players would need to play the game several times, each time making different choices.

To use KOTOR dialogue for my research, I extracted the game dialogue from the game and convert it to plain text.

## What's in the dataset?
Each datapoint (row) in the dataset (csv file) is one line of dialogue from Star Wars: Knights of the Old Republic.

Each datapoint has these columns:
- id: unique numerical identifier (assigned during dataset creation, has no meaning in the game)
- speaker: human readable name of the character that speaks the line. For NPCs: [firstname] + [lastname]. For PC: Player. 
- listener: human readable name of the character the speaker is speaking to. Probably used for head-turning 3D animations as well.
- text: dialogue line
- animation: animations that should be played for conversation participants. Might contain data for other characters (not speaker or listener) as well.
- comment: game developer/writer comments for this dialogue line
- next: possible follow-up dialogue lines (branching dialogue). Either the Player can choose, or the game uses conditional logic to choose.
- previous: the dialogue lines that possibly preceeded this line.
- source_dlg: the .dlg file from which this dialogue line is extracted. Generally there is 1 .dlg per character per planet. 
- audiofile: some dialogue lines have associated audio files with recordings of the voice actor. Extracting audio files is not (yet) covered in the instructions of this repo yet. 


## Creating the dataset from scratch
How to do data extraction from KOTOR:

1. clone this repo and navigate to SW:KOTOR folder
```
$ git clone https://github.com/hmi-utwente/video-game-text-corpora.git
$ cd video-game-text-corpora/
```
2. install [xoreos-tools](https://github.com/xoreos/xoreos-tools). More installation info on the [xoreos-wiki](https://wiki.xoreos.org/).
```
$ git clone https://github.com/xoreos/xoreos-tools.git
$ cd xoreos-tools/
$ sudo pacman -S zlib xz libxml2 boost boost-libs
$ /autogen.sh && ./configure && make
```
3. install python2 (if you don't have it already)
4. make a copy of your swkotor/ installation folder
5. extract all .dlg and .utc files from the game. These are compressed in swkotor/modules/*_s.rims and swkotor/data/templates.bif:
```
$ mkdir extracted # the `extracted/` folder should be in the same folder as `data/` and `src/`
$ cd extracted
$ for file in `ls ../swkotor/modules/*_s.rim`;do ../xoreos-tools/src/unrim e $file;done
$ ../xoreos-tools/src/unkeybif e ../swkotor/chitin.key ../swkotor/data/templates.bif
```
6. use my script to parse all `.dlg` and `.utc` files and re-assemble the dialogue trees from the game files. 
You can use the talktable file in the `data/` folder of my repository. This is the decompressed version of `swkotor/dialog.tlk`.
```
$ cd ../src
$ python2
>>> import char_dialog_pipeline as pipe
>>> dataset = pipe.create_dataset()
```
