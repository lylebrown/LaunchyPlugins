import os
from musicbeeipc import *
import launchy

class PyMusicbeeQueue(launchy.Plugin):
    def __init__(self):
        launchy.Plugin.__init__(self)
        self.name = "PyMusicbeeQueue"
        self.hash = launchy.hash(self.name)
        self.icon = os.path.join(launchy.getIconsPath(), "musicbee.png")

    def init(self):
        pass

    def getID(self):
        return self.hash

    def getName(self):
        return self.name

    def getIcon(self):
        return self.icon

    def getLabels(self, inputDataList):
        pass

    def getResults(self, inputDataList, resultsList):
        text = inputDataList[0].getText()
        resultsList.push_back( launchy.CatItem(text,
                                               "Play Song: " + text,
                                                self.getID(), self.getIcon()) )

    def getCatalog(self, resultsList):
        pass

    def launchItem(self, inputDataList, catItemOrig):
        catItem = inputDataList[-1].getTopResult()
        mbIPC = MusicBeeIPC()
        mbIPC.search_and_play_first(catItem.fullPath)


launchy.registerPlugin(PyMusicbeeQueue)