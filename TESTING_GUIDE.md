# cyberHunt Testing Guide

## Running Tests

To run the comprehensive test suite:

```bash
python -m pytest tests/test_compiler.py -v
```

Or using unittest directly:

```bash
python tests/test_compiler.py
```

## Test Coverage

The test suite covers:

### 1. Lexer Tests (`TestLexer`)
- ✅ Keyword tokenization
- ✅ String parsing
- ✅ Number parsing
- ✅ Operator tokenization
- ✅ Color code tokenization

### 2. Parser Tests (`TestParser`)
- ✅ Hello world program
- ✅ Variable assignment
- ✅ If statements
- ✅ While loops
- ✅ Function definitions

### 3. Interpreter Tests (`TestInterpreter`)
- ✅ String printing
- ✅ Variable assignment
- ✅ Arithmetic operations (add, subtract, multiply, divide)
- ✅ Comparison operators (>, <, ==)
- ✅ If-else statements
- ✅ While loops
- ✅ Function definition and calling
- ✅ Functions with return values
- ✅ Function parameters

### 4. Error Handling Tests (`TestErrorHandling`)
- ✅ Undefined variable errors
- ✅ Undefined function errors
- ✅ Division by zero errors

## Running Specific Tests

### Test only lexer:
```bash
python -m pytest tests/test_compiler.py::TestLexer -v
```

### Test only parser:
```bash
python -m pytest tests/test_compiler.py::TestParser -v
```

### Test only interpreter:
```bash
python -m pytest tests/test_compiler.py::TestInterpreter -v
```

### Test only error handling:
```bash
python -m pytest tests/test_compiler.py::TestErrorHandling -v
```

## Writing New Tests

### Example Test Template

```python
def test_my_feature(self):
    """Describe what this test does"""
    # Arrange: Set up test data
    code = 'shuro likho "test" khatam'
    
    # Act: Execute the code
    output = self.execute_code(code)
    
    # Assert: Check the result
    self.assertIn('test', output)
```

### Common Assertions

```python
# Check if substring is in output
self.assertIn('expected', output)

# Check equality
self.assertEqual(value, expected)

# Check if error is raised
with self.assertRaises(ValueError):
    # code that should raise error
    pass

# Check if True/False
self.assertTrue(condition)
self.assertFalse(condition)
```

## Example Programs to Test Manually

### Test 1: Basic Arithmetic
```bash
python compiler.py examples/math.ur
```

### Test 2: Conditions
```bash
python compiler.py examples/conditions.ur
```

### Test 3: Loops
```bash
python compiler.py examples/loops.ur
```

### Test 4: Functions
```bash
python compiler.py examples/function_basic.ur
python compiler.py examples/function_math.ur
python compiler.py examples/function_factorial.ur
```

## Test Output Example

```
$ python -m pytest tests/test_compiler.py -v

tests/test_compiler.py::TestLexer::test_keywords PASSED
tests/test_compiler.py::TestLexer::test_strings PASSED
tests/test_compiler.py::TestLexer::test_numbers PASSED
tests/test_compiler.py::TestParser::test_parse_hello_world PASSED
tests/test_compiler.py::TestInterpreter::test_print_string PASSED
tests/test_compiler.py::TestInterpreter::test_variable_assignment PASSED
tests/test_compiler.py::TestInterpreter::test_function_with_return PASSED
...

======================== 25 passed in 0.34s ========================
```

## Continuous Integration

To set up CI/CD with GitHub Actions:

1. Create `.github/workflows/tests.yml`
2. Add workflow configuration
3. Tests will run automatically on every push

## Debugging Tests

### Print Debug Info
```python
def test_debug(self):
    code = 'shuro likho "test" khatam'
    output = self.execute_code(code)
    print(f"Output: {repr(output)}")
    self.assertIn('test', output)
```

Run with:
```bash
python -m pytest tests/test_compiler.py::TestInterpreter::test_debug -v -s
```

### Check AST Structure
```python
def test_ast_structure(self):
    code = 'shuro likho "test" khatam'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST: {ast}")
```

## Performance Testing

For measuring execution time:

```python
import time

def test_performance(self):
    code = '''shuro
    i = 0
    jabbtak i chhota 1000
      i = i jodo 1
    khatam
    khatam'''
    
    start = time.time()
    self.execute_code(code)
    elapsed = time.time() - start
    
    print(f"Time: {elapsed}s")
    self.assertLess(elapsed, 1.0)  # Should complete in less than 1 second
```

---

**Happy Testing! 🧪**
