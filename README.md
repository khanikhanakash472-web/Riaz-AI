# cyberHunt - Roman Urdu Programming Language

A beginner-friendly programming language written entirely in Roman Urdu (Romanized Urdu script). Build console apps AND static websites!

## ✨ Features

- ✅ **Roman Urdu Syntax**: Write code in your native language
- ✅ **Simple & Intuitive**: Designed for beginners
- ✅ **Functions with Parameters & Returns**: Now fully functional!
- ✅ **Local & Global Scope**: Proper variable scoping
- ✅ **Color Support**: Built-in color and background color support
- ✅ **Web Framework**: Build static HTML websites in Urdu
- ✅ **Python-based Compiler**: Fast and reliable execution
- ✅ **Comprehensive Tests**: 25+ test cases included
- ✅ **Easy to Learn**: No complex symbols, just clear Roman Urdu words

## 🚀 What's New in This Version?

### Complete Functions Support! 🎉

Functions are now fully implemented with:
- ✅ Parameter passing
- ✅ Return values
- ✅ Local variable scoping
- ✅ Nested function calls
- ✅ Proper error handling

```roman urdu
shuro
  func add(a, b)
    return a jodo b
  khatam
  
  result = add(5, 3)
  likho "Total: " result
khatam
```

## 📦 Installation

```bash
git clone https://github.com/khanikhanakash472-web/Riaz-AI.git
cd Riaz-AI
python compiler.py your_file.ur
```

## 📚 Language Syntax

### Basic Structure

```roman urdu
shuro
  // Your code here
khatam
```

### Variables & Assignment

```roman urdu
naam = "Ahmed"
umar = 25
```

### Output (Print)

```roman urdu
likho "Hello World"
likho "#2 Green Text"
likho "##3 Blue Background"
likho "##2;#3 Green Background with Blue Text"
```

### Input

```roman urdu
naam = ?
naam = ? "Apka naam kya hai?"
```

### Conditions

```roman urdu
agar umar bara 18
  likho "Adult"
varna
  likho "Minor"
khatam
```

### Loops

```roman urdu
counter = 1
jabbtak counter chhota 10
  likho counter
  counter = counter jodo 1
khatam
```

### Functions (NEW!)

```roman urdu
func greet(name)
  likho "Salam " name
khatam

func add(a, b)
  return a jodo b
khatam

greet("Ali")
result = add(5, 3)
likho result
```

### Operators

#### Arithmetic
- `jodo` : Addition (+)
- `ghatao` : Subtraction (-)
- `gunaa` : Multiplication (*)
- `bhago` : Division (/)

#### Comparison
- `bara` : Greater than (>)
- `chhota` : Less than (<)
- `barabar` : Equal to (==)

#### Assignment
- `=` : Assign value

### Color Codes

#### Text Colors
- `#1` : Red
- `#2` : Green
- `#3` : Blue
- `#4` : Yellow
- `#5` : Purple
- `#6` : Cyan
- `#7` : White
- `#0` : Default

#### Background Colors
- `##1` : Red background
- `##2` : Green background
- `##3` : Blue background
- `##4` : Yellow background
- `##5` : Purple background
- `##6` : Cyan background
- `##7` : White background
- `##0` : Default background

#### Combined Usage
```roman urdu
likho "#2 Green Text"
likho "##3 Blue Background"
likho "##2;#3 Green Background with Blue Text"
```

## 🌐 Web Framework - Building Websites

### Web Elements Available

```roman urdu
page.add_heading("Title")
page.add_paragraph("Some text")
page.add_button("Click Me", "action")
page.add_link("Link Text", "url.html")
page.add_image("image.jpg", "Alt Text")
page.add_list(["Item 1", "Item 2", "Item 3"])
```

### Complete Website Example

```roman urdu
website = website_banao("MyAwesomeSite")

home = page_banao(website, "index", "Home")
home.add_heading("Mera Website")
home.add_paragraph("Ye mera pehla website hai")
home.add_link("About", "about.html")

about = page_banao(website, "about", "About")
about.add_heading("About Me")
about.add_paragraph("Main Riaz hoon")

generate_html(website)
```

## 📖 Example Programs

### Hello World

```roman urdu
shuro
  likho "#2 Khush Amdeed cyberHunt mein!"
  likho "Hello World!"
khatam
```

### With Input & Output

```roman urdu
shuro
  likho "Apka naam batao: "
  naam = ?
  likho "Salam " naam
khatam
```

### With Conditions

```roman urdu
shuro
  likho "Apki umar batao: "
  umar = ?
  agar umar bara 18
    likho "#2 Aap adult hain"
  varna
    likho "#1 Aap bacha hain"
  khatam
khatam
```

### With Loops

```roman urdu
shuro
  counter = 1
  jabbtak counter chhota 6
    likho "#3 Count: " counter
    counter = counter jodo 1
  khatam
khatam
```

### With Functions

```roman urdu
shuro
  func multiply(a, b)
    return a gunaa b
  khatam
  
  func calculate_total(price, quantity, tax_rate)
    subtotal = multiply(price, quantity)
    tax = subtotal gunaa tax_rate
    return subtotal jodo tax
  khatam
  
  total = calculate_total(100, 5, 0.1)
  likho "Total Price: " total
khatam
```

### Factorial Function

```roman urdu
shuro
  func factorial(n)
    result = 1
    counter = 1
    jabbtak counter barabar n
      result = result gunaa counter
      counter = counter jodo 1
    khatam
    return result
  khatam
  
  likho "5! = " factorial(5)
  likho "4! = " factorial(4)
khatam
```

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/test_compiler.py -v

# Or using unittest
python tests/test_compiler.py
```

**Test Coverage:**
- ✅ 25+ test cases
- ✅ Lexer tests
- ✅ Parser tests
- ✅ Interpreter tests
- ✅ Error handling tests
- ✅ Function tests

## 📁 Project Structure

```
cyberHunt/
├── README.md                    # This file
├── LANGUAGE_SPEC.md             # Language specification
├── FUNCTIONS_GUIDE.md           # Functions documentation
├── TESTING_GUIDE.md             # Testing guide
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT License
├── compiler.py                  # Main entry point
├── lexer.py                     # Tokenization
├── parser.py                    # AST building (with functions)
├── interpreter.py              # Execution engine (with functions)
├── functions.py                # Function management utilities
├── web_framework.py             # Static site generator
├── examples/
│   ├── hello_world.ur
│   ├── conditions.ur
│   ├── loops.ur
│   ├── math.ur
│   ├── colors.ur
│   ├── function_basic.ur        # NEW!
│   ├── function_math.ur         # NEW!
│   ├── function_factorial.ur    # NEW!
│   └── function_nested.ur       # NEW!
└── tests/
    └── test_compiler.py         # Comprehensive test suite
```

## 🎯 Quick Start

### 1. Console Program
```bash
python compiler.py examples/hello_world.ur
```

### 2. Custom Program
Create `mera_program.ur`:
```roman urdu
shuro
  likho "#2 Khush Amdeed!"
  likho "Apka naam kya hai?"
  naam = ?
  likho "Salam " naam
khatam
```

Then run:
```bash
python compiler.py mera_program.ur
```

### 3. With Functions
```bash
python compiler.py examples/function_math.ur
```

### 4. Test the Language
```bash
python -m pytest tests/test_compiler.py -v
```

## 📚 Documentation

- **[LANGUAGE_SPEC.md](LANGUAGE_SPEC.md)** - Complete language specification
- **[FUNCTIONS_GUIDE.md](FUNCTIONS_GUIDE.md)** - Detailed functions guide with examples
- **[TESTING_GUIDE.md](TESTING_GUIDE.md)** - How to write and run tests
- **[examples/](examples/)** - Sample programs
- **[LICENSE](LICENSE)** - MIT License

## 🗺️ Roadmap

- ✅ Console Programs
- ✅ Web Framework (Static Sites)
- ✅ **Functions & Advanced Features**
- ✅ **Local & Global Scoping**
- ✅ **Comprehensive Testing**
- 🔄 Database Support
- 🔄 Dynamic Web Apps
- 🔄 Mobile Apps
- 🔄 Recursion Support

## 🐛 Known Issues & Limitations

### Current Limitations
- ❌ No recursion support (yet)
- ❌ No default function parameters
- ❌ No variable arguments (*args)
- ❌ No dictionary/list data types (yet)
- ❌ No file I/O (yet)

### Error Handling
The language provides clear error messages:
- `SyntaxError` - Invalid syntax
- `NameError` - Undefined variable or function
- `ValueError` - Invalid value (e.g., division by zero)
- `TypeError` - Type mismatch

## 👨‍💻 Author

**Riaz Ali** (@riaz4764)

- Email: riaz.ai.studio@gmail.com
- GitHub: https://github.com/riaz4764

## 📄 License

MIT License - Free to use and modify. See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💬 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Contact: riaz.ai.studio@gmail.com
- Check documentation: [FUNCTIONS_GUIDE.md](FUNCTIONS_GUIDE.md)

## 🎓 Learning Resources

### Beginner
- Start with `examples/hello_world.ur`
- Move to `examples/conditions.ur`
- Then try `examples/loops.ur`

### Intermediate
- Learn functions in `examples/function_basic.ur`
- Practice math functions in `examples/function_math.ur`
- Study advanced patterns in `examples/function_nested.ur`

### Advanced
- Build websites with `web_framework.py`
- Study `parser.py` and `interpreter.py` for implementation details
- Contribute new features!

---

**Made with ❤️ for Urdu-speaking programmers**

**Urdu mein code likho. Apni language main soch. Duniya ko apne ideas de!**

---

## Version History

**v2.0.0** - Complete Functions Support (Current)
- ✅ Full function definition and calling
- ✅ Parameter passing
- ✅ Return values
- ✅ Local and global scoping
- ✅ 25+ test cases
- ✅ Comprehensive documentation

**v1.0.0** - Initial Release
- Console programs
- Web framework
- Basic features
