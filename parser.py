from lexer.py import Lexer, Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]

    def advance(self):
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]

    def parse(self):
        statements = []
        while self.current_token is not None:
            if self.current_token.token_type == 'IDENTIFIER':
                statements.append(self.assignment())
            elif self.current_token.token_type == 'NUMBER' or self.current_token.token_type == 'PLUS':
                statements.append(self.expression())
            else:
                self.advance()
        return statements

    def assignment(self):
        var_name = self.current_token.value
        self.advance()  # Move to '='
        self.advance()  # Move to value
        value = self.current_token.value
        self.advance()  # Move past value
        return ('ASSIGN', var_name, value)

    def expression(self):
        left = self.current_token.value
        self.advance()  # Move to operator
        operator = self.current_token.value
        self.advance()  # Move to right operand
        right = self.current_token.value
        self.advance()
        return ('EXPR', left, operator, right)
