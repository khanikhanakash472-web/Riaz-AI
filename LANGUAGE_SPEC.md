"""
cyberHunt Language Specification
Roman Urdu Programming Language - Complete Guide
"""

# LANGUAGE OVERVIEW
cyberHunt is a Roman Urdu programming language designed for beginners.
It uses simple Roman Urdu words instead of complex English keywords.

# BASIC SYNTAX

## Program Structure
shuro
  // code here
khatam

## Keywords

| Roman Urdu | English | Purpose |
|-----------|---------|---------|
| shuro | start | Begin program |
| khatam | end | End program/block |
| agar | if | Conditional statement |
| varna | else | Else clause |
| jabbtak | while | Loop statement |
| likho | print | Output |
| ? | input | Input |
| func | function | Function definition |
| return | return | Return value from function |

## Variables

Assignment:
  naam = "Ahmed"
  umar = 25
  price = 100.50

## Data Types

- Strings: "text" or 'text'
- Numbers: 10, 20, 3.14
- Booleans: True/False (from conditions)

## Operators

### Arithmetic
- jodo : Addition (+)
- ghatao : Subtraction (-)
- gunaa : Multiplication (*)
- bhago : Division (/)

### Comparison
- bara : Greater than (>)
- chhota : Less than (<)
- barabar : Equal to (==)

### Assignment
- = : Assign value

## Color System

### Text Colors (Single #)
#0 : Default
#1 : Red
#2 : Green
#3 : Blue
#4 : Yellow
#5 : Purple
#6 : Cyan
#7 : White

### Background Colors (Double ##)
##0 : Default
##1 : Red background
##2 : Green background
##3 : Blue background
##4 : Yellow background
##5 : Purple background
##6 : Cyan background
##7 : White background

### Combined Format
"##background;#textcolor Text"
Example: "##2;#3 Green Background with Blue Text"

## Conditional Statements

agar condition
  // true block
varna
  // false block
khatam

## Loops

jabbtak condition
  // loop body
khatam

## Input/Output

Print:
  likho "message"
  likho "#2 green message"
  likho "##3 text with blue background"

Input:
  naam = ?
  naam = ? "Prompt message here?"

## Comments

// This is a comment

## FUNCTIONS (NEW!)

### Function Definition

func function_name(param1, param2)
  // Function body
  // Local variables here
  return result
khatam

### Function Calling

result = function_name(arg1, arg2)
likho result

### Function with Parameters

func add(a, b)
  return a jodo b
khatam

sum = add(5, 3)
likho sum

### Function with Return Statement

func greet(name)
  likho "Salam " name
  return "Done"
khatam

output = greet("Ali")

### Local Variables

Variables defined inside functions are local to that function:

func test()
  local_var = "Inside"
  likho local_var
khatam

test()
likho local_var  // Error: not defined

### Global Variables

Variables defined outside functions can be accessed inside:

global_var = "Outside"

func test()
  likho global_var  // OK
khatam

test()

### Nested Function Calls

func add(a, b)
  return a jodo b
khatam

func double_sum(x, y)
  sum = add(x, y)
  return sum gunaa 2
khatam

result = double_sum(3, 4)
likho result  // 14

## EXAMPLES

### Hello World
shuro
  likho "#2 Hello, World!"
khatam

### Simple Math
shuro
  a = 5
  b = 10
  sum = a jodo b
  likho "Result: " sum
khatam

### User Input
shuro
  likho "Your name: "
  naam = ?
  likho "#3 Shukriya " naam
khatam

### Conditions
shuro
  age = 20
  agar age bara 18
    likho "#2 Adult"
  varna
    likho "#1 Minor"
  khatam
khatam

### Loops
shuro
  counter = 1
  jabbtak counter chhota 6
    likho "#3 Count: " counter
    counter = counter jodo 1
  khatam
khatam

### Functions
shuro
  func multiply(x, y)
    return x gunaa y
  khatam
  
  func calculate_area(length, width)
    return multiply(length, width)
  khatam
  
  area = calculate_area(5, 10)
  likho "Area: " area
khatam

### Factorial with Function
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
khatam

## EXECUTION

Command:
  python compiler.py program.ur

Process:
  Lexer tokenizes the code
  Parser builds AST
  Interpreter executes AST

## ERROR HANDLING

- SyntaxError: Invalid syntax
- NameError: Undefined variable or function
- ValueError: Invalid value (e.g., division by zero)
- TypeError: Type mismatch

## SCOPE AND VARIABLES

### Global Scope
Variables defined at program level (outside functions)

global_var = 10

func test()
  likho global_var  // Can access
khatam

### Local Scope
Variables defined inside functions

func test()
  local_var = "Local"
  likho local_var  // OK
khatam

likho local_var  // Error: not defined

### Scope Rules
1. Local variables shadow global variables
2. Function parameters are local to that function
3. Modifications in local scope don't affect global scope
4. Return values allow communication between scopes

## BEST PRACTICES

1. Use meaningful variable names
  naam = "Ahmed"  // Good
  n = "Ahmed"     // Not clear

2. Add comments for clarity
  // Calculate total price with tax
  total = price jodo tax

3. Use proper indentation
  agar condition
    likho "Indented"
  khatam

4. Test with simple examples first

5. Use functions to organize code
  func calculate_tax(price)
    return price gunaa 0.1
  khatam

6. Use colors for better UI
  likho "#2 Success: Operation completed"

## LIMITATIONS

Current version:
- ✅ Functions with parameters and return values
- ✅ Local and global variable scoping
- ✅ Basic data types (strings, numbers)
- ❌ No recursion (yet)
- ❌ No default function parameters
- ❌ No variable arguments (*args)
- ❌ No arrays/lists
- ❌ No dictionaries
- ❌ No file I/O

## VERSION

Version: 2.0.0
Author: Riaz Ali (@riaz4764)
License: MIT
Last Updated: 2026-07-09

## CHANGES FROM v1.0.0

- Added complete function support
- Added parameter passing
- Added return values
- Added local/global scoping
- Enhanced error handling
- Added comprehensive tests
- Added detailed documentation

For more information, see:
- FUNCTIONS_GUIDE.md - Detailed functions guide
- TESTING_GUIDE.md - Testing information
- README.md - Main documentation
