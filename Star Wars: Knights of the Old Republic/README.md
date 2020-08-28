# Star Wars: Knights of the Old Republic 

## Creating the dataset from scratch
How to do data extraction from KOTOR:

1. clone this repo and navigate to SW:KOTOR folder
```
$ git clone https://github.com/hmi-utwente/video-game-text-corpora.git
$ cd video-game-text-corpora/
```
2. install [xoreos-tools](). More installation info on the xoreos-wiki.
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
6. use my script to parse all dlg and utc files and re-assemble the dialogue trees from the game files. 
You can use the talktable (decompressed version of swkotor/dialog.tlk) file in the date folder of my repository.
```
$ cd ../src
$ python2
>>> import char_dialog_pipeline as pipe
>>> pipe.main()
```
