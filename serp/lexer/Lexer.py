from serp.utils import FilePath, FileHandler

class Lexer:
    def __init__(self, filePath: FilePath):
        self.filePath = filePath
        self.tokens = {}

        print(FileHandler(filePath).getContent())