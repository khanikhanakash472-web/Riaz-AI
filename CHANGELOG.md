# Changelog

All notable changes to cyberHunt will be documented in this file.

## [2.0.0] - 2026-07-09

### Added
- ✅ **Complete Functions Support**
  - Function definition with `func` keyword
  - Parameter passing to functions
  - Return values with `return` keyword
  - Local variable scoping in functions
  - Global variable access from functions
  - Nested function calls

- ✅ **New Module: functions.py**
  - Function management utilities
  - Function class for storing definitions
  - FunctionManager for scope management

- ✅ **Enhanced Parser (parser.py)**
  - `parse_function_def()` - Parse function definitions
  - `parse_assignment_or_input_or_call()` - Handle function calls
  - Function call parsing in expressions
  - Support for function parameters and arguments

- ✅ **Enhanced Interpreter (interpreter.py)**
  - `define_function()` - Register function definitions
  - `call_function()` - Execute user-defined functions
  - Local scope management with `local_variables` stack
  - Proper variable scoping (local and global)
  - Function call evaluation in expressions

- ✅ **Comprehensive Test Suite (tests/test_compiler.py)**
  - 25+ test cases covering:
    - Lexer tokenization
    - Parser AST construction
    - Interpreter execution
    - Function definition and calling
    - Error handling

- ✅ **Documentation**
  - FUNCTIONS_GUIDE.md - Detailed functions documentation with examples
  - TESTING_GUIDE.md - Testing guide with instructions and examples
  - Enhanced README.md with new features

- ✅ **Example Programs**
  - examples/function_basic.ur - Basic function usage
  - examples/function_math.ur - Math operations with functions
  - examples/function_factorial.ur - Factorial calculation
  - examples/function_nested.ur - Nested function calls

### Changed
- Updated LANGUAGE_SPEC.md to include function syntax
- Improved error messages for better debugging
- Enhanced README with function examples

### Fixed
- Better error handling for undefined functions
- Proper variable scoping in nested function calls
- Fixed division by zero error handling

### Performance
- Optimized function call execution
- Efficient scope management

## [1.0.0] - 2026-07-08

### Added
- Initial release of cyberHunt programming language
- Roman Urdu syntax support
- Basic features:
  - Variables and assignment
  - Print output (likho)
  - User input (?)
  - Conditionals (agar/varna)
  - Loops (jabbtak)
  - Arithmetic operators (jodo, ghatao, gunaa, bhago)
  - Comparison operators (bara, chhota, barabar)
  - Color support for console output
- Web framework for building static HTML websites
- Python-based compiler with:
  - Lexer for tokenization
  - Parser for AST construction
  - Interpreter for execution
- Example programs
- MIT License

---

## Upgrade Guide: v1.0.0 → v2.0.0

### New Syntax

#### Function Definition
```roman urdu
func function_name(param1, param2)
  // Function body
  return result
khatam
```

#### Function Calling
```roman urdu
result = function_name(arg1, arg2)
```

### Breaking Changes
None - all existing code is compatible!

### Migration Notes
- Existing programs will continue to work without modifications
- New function features are optional
- Gradually migrate to functions for better code organization

---

## Future Roadmap

### v2.1.0 (Planned)
- [ ] Recursion support
- [ ] Default function parameters
- [ ] Variable arguments (*args)

### v2.2.0 (Planned)
- [ ] List/Array data type
- [ ] Dictionary data type
- [ ] String manipulation functions

### v3.0.0 (Planned)
- [ ] File I/O support
- [ ] Database connectivity
- [ ] Module/Import system

### v4.0.0 (Planned)
- [ ] Dynamic web applications
- [ ] Mobile app compilation
- [ ] Package manager

---

## Support

For detailed information about changes, see:
- [FUNCTIONS_GUIDE.md](FUNCTIONS_GUIDE.md) - Functions documentation
- [TESTING_GUIDE.md](TESTING_GUIDE.md) - Testing information
- [LANGUAGE_SPEC.md](LANGUAGE_SPEC.md) - Language specification
- [README.md](README.md) - Main documentation

---

**Made with ❤️ for Urdu-speaking programmers**
