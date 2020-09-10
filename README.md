# video-game-text-corpora
Data and code for a paper about video game text corpora.

## Datasets

- Torchlight II quest texts: quest dialogue, main quest summaries and GUI text in [CSV-format](https://github.com/hmi-utwente/video-game-text-corpora/raw/master/Torchlight%20II/data/dataset_200630.csv).
- Star Wars: Knights of the Old republic: branching player and NPC dialogue in [CSV-format](https://github.com/hmi-utwente/video-game-text-corpora/blob/master/Star%20Wars:%20Knights%20of%20the%20Old%20Republic/data/dataset_20200716.csv?raw=true).
- The Elder Scrolls (Arena, Daggerfall, Morrowind, Oblivion, Skyrim and The Elder Scrolls: Online): in-game books in [JSON-format](https://github.com/hmi-utwente/video-game-text-corpora/blob/master/The%20Elder%20Scrolls/data/imperial_library_20200626.json?raw=true).

## Code

Each game-folder has a `src/` folder that contains the code for creating the dataset. 
It should give some insight in how the data was extracted. 

For TorchLight II and SW:KOTOR: 
before you can run the code, you should have access to the original game files from which the data was extracted. 

## Scientific paper

This repository is for the research paper *Fantastic Strings and Where to Find Them: The Quest for High-Quality Video Game Text Corpora*, 
to appear in the proceedings of [INT 2020](https://sites.google.com/view/int2020/home). 
[Preprint version of the paper](https://judithvanstegeren.com/assets/2008-vanstegeren2020fantastic-preprint.pdf).
If you use the data or code, please cite the following paper:

```
@inproceedings{vanstegeren2020fantastic,
    title = "{Fantastic Strings and Where to Find Them: The Quest for High-Quality Video Game Text Corpora}",
    author = {van Stegeren, Judith and Theune, Mari{\"e}t},
    booktitle = "Intelligent Narrative Technologies Workshop",
    month = oct,
    year = "2020",
    publisher = {AAAI Press},
}
```
The corpora were extracted from three commercial video games. The games and the game assets are copyright the respective game publishers and game developers. If you use the datasets, don't forget to cite the games too!
```
@misc{game:starwarsknightsoftheoldrepublic,
title = {\emph{Star Wars: Knights of the Old Republic}},
year = {2003},
organization = {LucasArts},
publisher = {LucasArts},
author = {{BioWare}},
Howpublished = {Game [PC]},
Note = {LucasArts, San Francisco, US},
}

@misc{game:torchlight2,
title = {\emph{Torchlight II}},
year = {2012},
organization = {Runic Games},
publisher = {Runic Games},
author = {{Runic Games}},
Howpublished = {Game [PC]},
Note = {Runic Games, Seattle, Washington, US},
}

@misc{gamesseries:tes,
title = {\emph{The Elder Scrolls I-V} and \emph{The Elder Scrolls Online}},
date = {1994/2014},
year = {1994--2014},
organization = {Bethesda Softworks},
publisher = {Bethesda Softworks},
author = {{Bethesda Softworks}},
Howpublished = {Game series [PC]},
Note = {Bethesda Softworks, Rockville, Maryland, US},
}
```
