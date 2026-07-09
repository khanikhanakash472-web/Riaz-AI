"""
cyberHunt Comprehensive Test Suite
Tests for lexer, parser, and interpreter
"""

import unittest
import sys
import os
from io import StringIO

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexer import Lexer, TokenType
from parser import Parser
from interpreter import Interpreter

class TestLexer(unittest.TestCase):
    """Test lexer tokenization"""
    
    def test_keywords(self):
        """Test keyword tokenization"""
        code = "shuro khatam likho agar varna jabbtak func return"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        token_types = [t.type for t in tokens[:-1]]  # Exclude EOF
        expected = [
            TokenType.SHURO, TokenType.KHATAM, TokenType.LIKHO,
            TokenType.AGAR, TokenType.VARNA, TokenType.JABBTAK,
            TokenType.FUNC, TokenType.RETURN
        ]
        self.assertEqual(token_types, expected)
    
    def test_strings(self):
        """Test string tokenization"""
        code = '"hello" \'world\''
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.STRING)
        self.assertEqual(tokens[0].value, "hello")
        self.assertEqual(tokens[1].type, TokenType.STRING)
        self.assertEqual(tokens[1].value, "world")
    
    def test_numbers(self):
        """Test number tokenization"""
        code = "10 3.14 100"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].value, 10)
        self.assertEqual(tokens[1].value, 3.14)
        self.assertEqual(tokens[2].value, 100)
    
    def test_operators(self):
        """Test operator tokenization"""
        code = "jodo ghatao gunaa bhago bara chhota barabar"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        token_types = [t.type for t in tokens[:-1]]
        expected = [
            TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY,
            TokenType.DIVIDE, TokenType.GREATER, TokenType.LESS,
            TokenType.EQUAL
        ]
        self.assertEqual(token_types, expected)
    
    def test_colors(self):
        """Test color code tokenization"""
        code = "#2 ##3"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.COLOR_TEXT)
        self.assertEqual(tokens[0].value, 2)
        self.assertEqual(tokens[1].type, TokenType.COLOR_BG)
        self.assertEqual(tokens[1].value, 3)

class TestParser(unittest.TestCase):
    """Test parser AST construction"""
    
    def test_parse_hello_world(self):
        """Test parsing hello world program"""
        code = 'shuro likho "Hello" khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        self.assertEqual(ast['type'], 'program')
        self.assertEqual(len(ast['statements']), 1)
        self.assertEqual(ast['statements'][0]['type'], 'likho')
    
    def test_parse_assignment(self):
        """Test parsing variable assignment"""
        code = 'shuro naam = "Ahmed" khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        stmt = ast['statements'][0]
        self.assertEqual(stmt['type'], 'assignment')
        self.assertEqual(stmt['name'], 'naam')
    
    def test_parse_if_statement(self):
        """Test parsing if statement"""
        code = 'shuro agar 5 bara 3 likho "yes" khatam khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        stmt = ast['statements'][0]
        self.assertEqual(stmt['type'], 'if')
        self.assertIn('condition', stmt)
        self.assertIn('then_body', stmt)
    
    def test_parse_while_loop(self):
        """Test parsing while loop"""
        code = 'shuro i = 1 jabbtak i chhota 5 likho i i = i jodo 1 khatam khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Should have assignment and while loop
        self.assertTrue(any(s['type'] == 'while' for s in ast['statements']))
    
    def test_parse_function_def(self):
        """Test parsing function definition"""
        code = 'shuro func add(a, b) likho a khatam khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        
        stmt = ast['statements'][0]
        self.assertEqual(stmt['type'], 'function_def')
        self.assertEqual(stmt['name'], 'add')
        self.assertEqual(stmt['parameters'], ['a', 'b'])

class TestInterpreter(unittest.TestCase):
    """Test interpreter execution"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
    
    def tearDown(self):
        """Restore stdout"""
        sys.stdout = sys.__stdout__
    
    def execute_code(self, code):
        """Helper to execute code and return output"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        interpreter.execute(ast)
        return self.captured_output.getvalue()
    
    def test_print_string(self):
        """Test printing strings"""
        code = 'shuro likho "Hello World" khatam'
        output = self.execute_code(code)
        self.assertIn('Hello World', output)
    
    def test_variable_assignment(self):
        """Test variable assignment and retrieval"""
        code = 'shuro name = "Ahmed" likho name khatam'
        output = self.execute_code(code)
        self.assertIn('Ahmed', output)
    
    def test_arithmetic(self):
        """Test arithmetic operations"""
        code = 'shuro result = 5 jodo 3 likho result khatam'
        output = self.execute_code(code)
        self.assertIn('8', output)
    
    def test_subtraction(self):
        """Test subtraction"""
        code = 'shuro result = 10 ghatao 4 likho result khatam'
        output = self.execute_code(code)
        self.assertIn('6', output)
    
    def test_multiplication(self):
        """Test multiplication"""
        code = 'shuro result = 3 gunaa 4 likho result khatam'
        output = self.execute_code(code)
        self.assertIn('12', output)
    
    def test_division(self):
        """Test division"""
        code = 'shuro result = 20 bhago 4 likho result khatam'
        output = self.execute_code(code)
        self.assertIn('5', output)
    
    def test_comparison_greater(self):
        """Test greater than comparison"""
        code = 'shuro agar 5 bara 3 likho "yes" khatam khatam'
        output = self.execute_code(code)
        self.assertIn('yes', output)
    
    def test_comparison_less(self):
        """Test less than comparison"""
        code = 'shuro agar 2 chhota 5 likho "yes" khatam khatam'
        output = self.execute_code(code)
        self.assertIn('yes', output)
    
    def test_if_else(self):
        """Test if-else statement"""
        code = 'shuro agar 1 bara 2 likho "yes" varna likho "no" khatam khatam'
        output = self.execute_code(code)
        self.assertIn('no', output)
    
    def test_while_loop(self):
        """Test while loop"""
        code = 'shuro i = 1 jabbtak i chhota 4 likho i i = i jodo 1 khatam khatam'
        output = self.execute_code(code)
        self.assertIn('1', output)
        self.assertIn('2', output)
        self.assertIn('3', output)
    
    def test_function_definition_and_call(self):
        """Test function definition and calling"""
        code = '''shuro
        func greet(name)
            likho "Salam " name
        khatam
        greet("Ali")
        khatam'''
        output = self.execute_code(code)
        self.assertIn('Salam', output)
        self.assertIn('Ali', output)
    
    def test_function_with_return(self):
        """Test function with return value"""
        code = '''shuro
        func add(a, b)
            return a jodo b
        khatam
        result = add(3, 5)
        likho result
        khatam'''
        output = self.execute_code(code)
        self.assertIn('8', output)
    
    def test_function_with_parameters(self):
        """Test function parameter passing"""
        code = '''shuro
        func multiply(x, y)
            return x gunaa y
        khatam
        ans = multiply(4, 5)
        likho ans
        khatam'''
        output = self.execute_code(code)
        self.assertIn('20', output)

class TestErrorHandling(unittest.TestCase):
    """Test error handling"""
    
    def test_undefined_variable(self):
        """Test undefined variable error"""
        code = 'shuro likho undefined_var khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        
        with self.assertRaises(NameError):
            interpreter.execute(ast)
    
    def test_undefined_function(self):
        """Test undefined function error"""
        code = 'shuro foo() khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        
        with self.assertRaises(NameError):
            interpreter.execute(ast)
    
    def test_division_by_zero(self):
        """Test division by zero error"""
        code = 'shuro result = 5 bhago 0 khatam'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        
        with self.assertRaises(ValueError):
            interpreter.execute(ast)

if __name__ == '__main__':
    unittest.main()
