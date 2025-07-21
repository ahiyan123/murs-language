import unittest
from interpreter import Interpreter

class TestMarsInterpreter(unittest.TestCase):
    def test_assignment(self):
        code = "x = 5"
        interpreter = Interpreter(code)
        interpreter.interpret()
        self.assertEqual(interpreter.variables['x'], 5)

    def test_expression(self):
        code = "x = 5\ny = 10\nx + y"
        interpreter = Interpreter(code)
        result = interpreter.interpret()
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
