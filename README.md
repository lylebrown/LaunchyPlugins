LaunchyPlugins
==============

Plugins for [Launchy](http://www.launchy.net/), a cross-platform application launcher.

## Contents
1. pyEverything
2. PyMusicbeeQueue
3. Disclaimer

### pyEverything

Launches the [Everything search engine](http://www.voidtools.com/) with the query provided.

#### pyEverything Setup

1. Change the 'everythingPath' variable to the location of Everything.exe on your system. 
2. Install Python 2.7 (x32).
3. Install [PyLaunchy](http://sourceforge.net/projects/pylaunchy/files/pylaunchy/).
4. Copy pyEverything.py to *LaunchyFolder*\plugins\python
5. Copy everything.png to *LaunchyFolder*\plugins\icons
6. Configure Launchy to run as Administrator (for all users, if applicable)

### PyMusicbeeQueue

Immediately adds the first song in the library matching the given description to the queue and plays it.

**This plugin may frequently change, as it's more for personal development.** Requests? Add them to the bug tracker, and I'll either make a special release just for you, or a configurable master release in the future.

#### PyMusicBeeQueue Setup

1. Install Python 2.7 (x32).
2. Install [PyLaunchy](http://sourceforge.net/projects/pylaunchy/files/pylaunchy/).
3. Assuming you have Musicbee installed, add [MusicBeeIPC](http://getmusicbee.com/forum/index.php?topic=11492.0) to your plugins folder.
4. Copy PyMusicbeeQueue.py to *LaunchyFolder*\plugins\python
5. Copy musicbee.png to *LaunchyFolder*\plugins\icons
6. Configure Launchy and Musicbee to run as Administrator (for all users, if applicable)


### Disclaimer

All of these plugins have been developed for Windows. Use on other operating systems may require modification; feel free to fork if you go this route.
