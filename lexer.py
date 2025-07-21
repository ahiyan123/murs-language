import re

# Define token types
TOKEN_TYPES = [
    ('NUMBER', r'\b\d+\b'),       # Integer
    ('PLUS', r'\+'),              # Addition
    ('MINUS', r'-'),              # Subtraction
    ('MUL', r'\*'),               # Multiplication
    ('DIV', r'/'),                # Division
    ('ASSIGN', r'='),             # Assignment
    ('IDENTIFIER', r'\b[a-zA-Z]\w*\b'),  # Variable names
    ('NEWLINE', r'\n'),           # Newline
    ('SPACE', r'[ \t]+'),         # Spaces
    ('SKIP', r'[^\s]'),           # Unrecognized characters
]

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value
    
    def __repr__(self):
        return f'Token({self.token_type}, {self.value})'

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.current_char = self.source_code[self.position]
    
    def advance(self):
        """Move to the next character."""
        self.position += 1
        if self.position < len(self.source_code):
            self.current_char = self.source_code[self.position]
        else:
            self.current_char = None

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            for token_type, regex in TOKEN_TYPES:
                if re.match(regex, self.current_char):
                    if token_type == 'NUMBER':
                        value = self.collect_number()
                        tokens.append(Token(token_type, value))
                    elif token_type == 'IDENTIFIER':
                        value = self.collect_identifier()
                        tokens.append(Token(token_type, value))
                    elif token_type == 'NEWLINE':
                        tokens.append(Token(token_type, self.current_char))
                        self.advance()
                    elif token_type == 'SPACE':
                        self.advance()  # Ignore space
                    elif token_type == 'SKIP':
                        raise Exception(f"Unexpected character: {self.current_char}")
                    else:
                        tokens.append(Token(token_type, self.current_char))
                        self.advance()
                    break
        return tokens

    def collect_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def collect_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result
