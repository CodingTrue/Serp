import enum

class TokenType(enum.Enum):
    INDENTATION     = "INDEN"
    STRING_LITERAL  = "STR_LIT"
    NUMBER_LITERAL  = "NUM_LIT"
    EOL             = "EOL"
    EOF             = "EOF"
    DQUOTE          = "DQUOTE"
    SQUOTE          = "SQUOTE"
    PLUS            = "PLUS"
    MINUS           = "MINUS"
    ARROW_OPEN      = "ARW_OP"
    ARROW_CLOSED    = "ARW_CL"
    COLON           = "COL"
    COMMA           = "COMMA"
    LPAREN          = "LPAREN"
    RPAREN          = "RPAREN"

class Token:
    def __init__(self, type: TokenType, value: any):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type}{':' + str(self.value) if self.value else ''}"