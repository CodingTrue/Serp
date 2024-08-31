from serp.utils import FilePath, FileHandler
from serp.lexer.Token import TokenType, Token
from string import ascii_letters, digits

EOF_CHAR = "EOF_CHAR"
EOL_CHAR = "EOL_CHAR"

WHITESPACE = " \t\n"

STRING_BEGIN = ascii_letters + "_"
STRING_ALLOWED = STRING_BEGIN + digits

NUMBER_BEGIN = digits + "."
NUMBER_ALLOWED = NUMBER_BEGIN + "_"

class Lexer:
    def __init__(self, filePath: FilePath):
        self.filePath = filePath
        self.file = FileHandler(self.filePath)
        self.tokens = []

        self.text = self.file.getContent()
        self.text_len = len(self.text)
        self.char = ''
        self.pos = -1
        self.row = 0
        self.column = 1

    def add_token(self, token_type: TokenType, value: any = ""):
        self.tokens.append(Token(type=token_type, value=value))

    def advance(self):
        self.pos += 1
        self.column += 1
        self.char = self.text[self.pos] if self.pos < self.text_len else EOF_CHAR

        if self.char == '\n':
            self.column = 0
            self.row += 1

    def lex(self):
        self.tokens.clear()

        while not (self.char == EOF_CHAR):
            if self.char in STRING_BEGIN:
                self.add_token(TokenType.STRING_LITERAL, self.generate_string_literal())

            elif self.char in NUMBER_BEGIN:
                self.add_token(TokenType.NUMBER_LITERAL, self.generate_number_literal())
            elif self.char in WHITESPACE:
                self.add_token(TokenType.INDENTATION)
                self.advance()
            elif self.char == "(":
                self.add_token(TokenType.LPAREN)
                self.advance()
            elif self.char == ")":
                self.add_token(TokenType.RPAREN)
                self.advance()
            elif self.char == ":":
                self.add_token(TokenType.COLON)
                self.advance()
            elif self.char == ",":
                self.add_token(TokenType.COMMA)
                self.advance()
            elif self.char == "+":
                self.add_token(TokenType.PLUS)
                self.advance()
            elif self.char == "-":
                self.add_token(TokenType.MINUS)
                self.advance()
            elif self.char == "<":
                self.add_token(TokenType.ARROW_OPEN)
                self.advance()
            elif self.char == ">":
                self.add_token(TokenType.ARROW_CLOSED)
                self.advance()
            elif self.char == '"':
                self.add_token(TokenType.DQUOTE)
                self.advance()
            elif self.char == "'":
                self.add_token(TokenType.SQUOTE)
                self.advance()
            else:
                # error reporting will be implmented next
                raise Exception(f"Unkown char '{self.char}' in file {self.filePath.getFilename()} at line {self.row}:{self.column}")

    def generate_string_literal(self) -> str:
        result = ""

        while self.char in STRING_ALLOWED:
            result += self.char
            self.advance()
        return result

    def generate_number_literal(self) -> [int, float]:
        result = ""
        dot_count = 0

        # add restrictions for prefixed bases
        while self.char in NUMBER_ALLOWED:
            result += self.char

            if self.char == ".":
                dot_count += 1
                if dot_count > 1: raise Exception("Too many dots for a float!")
            self.advance()
        return int(result) if dot_count == 0 else float(result)