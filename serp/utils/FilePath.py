from os.path import realpath, isfile, isdir

class FilePath:
    def __init__(self, path: str):
        self.path = realpath(path)

        if self.isDir() or self.isEmpty():
            exit(-1)  # error: filepath is a directory or empty!

    def getPath(self) -> str: return self.path
    def setPeth(self, path: str): self.path = path

    def isFile(self) -> bool: return isfile(self.getPath())
    def isDir(self) -> bool: return isdir(self.getPath())
    def isEmpty(self) -> bool: return self.path == ""

    def getFilename(self) -> str: return self.getPath().split("\\")[-1]
    def getPureFilename(self) -> str: return self.getPath().split("\\")[-1].split(".")[0]

    def __repr__(self):
        return f"FP_{id(self)}[{self.getPath()}]"