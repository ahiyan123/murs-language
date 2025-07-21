from parser.py import Parser
from lexer.py import Lexer

class Interpreter:
    def __init__(self, statements):
        self.statements = statements
        self.variables = {}

    def interpret(self):
        for statement in self.statements:
            if statement[0] == 'ASSIGN':
                var_name = statement[1]
                value = int(statement[2])
                self.variables[var_name] = value
            elif statement[0] == 'EXPR':
                left = int(statement[1])
                operator = statement[2]
                right = int(statement[3])
                if operator == '+':
                    result = left + right
                elif operator == '-':
                    result = left - right
                elif operator == '*':
                    result = left * right
                elif operator == '/':
                    result = left / right
                print("Result:", result)

# Main execution
if __name__ == "__main__":
    code = """x = 5
               y = 10
               x + y"""
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    statements = parser.parse()

    interpreter = Interpreter(statements)
    interpreter.interpret()
