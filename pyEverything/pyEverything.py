from subprocess import call
import os
import launchy

# VARIABLES
everythingPath = "C:\\Program Files (x86)\\Everything\\Everything.exe"

class pyEverything(launchy.Plugin):
    def __init__(self):
        launchy.Plugin.__init__(self)
        self.name = "pyEverything"
        self.hash = launchy.hash(self.name)
        self.icon = os.path.join(launchy.getIconsPath(), "everything.png")

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
            "pyEverything: " + text,
            self.getID(), self.getIcon()) )

    def getCatalog(self, resultsList):
        pass

    def launchItem(selfself, inputDataList, catItemOrig):
        catItem = inputDataList[-1].getTopResult()
        call([everythingPath, "-search", catItem.fullPath])

launchy.registerPlugin(pyEverything)