from serp.utils import FilePath

class FileHandler:
    def __init__(self, filePath: FilePath):
        self.filePath = filePath

    def getFilePath(self): return self.filePath
    def setFilePath(self, filePath: FilePath): self.filePath = filePath

    def getContent(self):
        with open(self.filePath.getPath(), "r") as f:
            content = f.read()
            f.close()
        return content