from serp.utils import FilePath, FileHandler

class Lexer:
    def __init__(self, filePath: FilePath):
        self.filePath = filePath

        print(FileHandler(filePath).getContent())