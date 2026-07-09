# cyberHunt Functions Guide

## Function Definition (func)

Functions in cyberHunt allow you to organize code into reusable blocks. Define a function using the `func` keyword:

```roman urdu
func function_name(parameter1, parameter2)
  // Function body
  // Your code here
khatam
```

## Syntax

### Basic Function

```roman urdu
shuro
  func greet(name)
    likho "Salam " name
  khatam
  
  greet("Ahmed")  // Function call
khatam
```

**Output:**
```
Salam Ahmed
```

### Function with Return Value

Use the `return` keyword to return a value from a function:

```roman urdu
shuro
  func add(a, b)
    result = a jodo b
    return result
  khatam
  
  sum = add(5, 3)
  likho "Sum: " sum
khatam
```

**Output:**
```
Sum: 8
```

### Function Parameters

Functions can accept multiple parameters:

```roman urdu
shuro
  func multiply(x, y, z)
    return x gunaa y gunaa z
  khatam
  
  answer = multiply(2, 3, 4)
  likho answer
khatam
```

**Output:**
```
24
```

## Examples

### Example 1: Simple Greeting Function

```roman urdu
shuro
  func welcome(user)
    likho "#2 Khush Amdeed, " user
    likho "Welcome to cyberHunt!"
  khatam
  
  welcome("Riaz")
  welcome("Ali")
khatam
```

### Example 2: Math Functions

```roman urdu
shuro
  func square(n)
    return n gunaa n
  khatam
  
  func cube(n)
    return n gunaa n gunaa n
  khatam
  
  likho "Square of 5: " square(5)
  likho "Cube of 3: " cube(3)
khatam
```

### Example 3: Function with Conditionals

```roman urdu
shuro
  func isAdult(age)
    agar age bara 18
      return "Adult"
    varna
      return "Minor"
    khatam
  khatam
  
  likho isAdult(25)
  likho isAdult(15)
khatam
```

### Example 4: Function with Loops

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
khatam
```

### Example 5: Multiple Functions Working Together

```roman urdu
shuro
  func celsius_to_fahrenheit(c)
    return c gunaa 9 bhago 5 jodo 32
  khatam
  
  func print_temperature(celsius)
    fahrenheit = celsius_to_fahrenheit(celsius)
    likho celsius " C = " fahrenheit " F"
  khatam
  
  print_temperature(0)
  print_temperature(25)
  print_temperature(100)
khatam
```

## Scope and Variables

### Local Variables

Variables defined inside a function are **local** to that function:

```roman urdu
shuro
  func test()
    local_var = "Inside"
    likho local_var
  khatam
  
  test()
  likho local_var  // Error: local_var not defined
khatam
```

### Global Variables

Variables defined outside functions are **global**:

```roman urdu
shuro
  global_var = "Outside"
  
  func test()
    likho global_var  // Can access global_var
  khatam
  
  test()
khatam
```

## Common Patterns

### Pattern 1: Function that Modifies State

```roman urdu
shuro
  counter = 0
  
  func increment()
    counter = counter jodo 1
    return counter
  khatam
  
  likho increment()  // 1
  likho increment()  // 2
  likho increment()  // 3
khatam
```

### Pattern 2: Function with Conditional Return

```roman urdu
shuro
  func max(a, b)
    agar a bara b
      return a
    varna
      return b
    khatam
  khatam
  
  likho max(10, 20)  // 20
khatam
```

### Pattern 3: Function Calling Another Function

```roman urdu
shuro
  func add(a, b)
    return a jodo b
  khatam
  
  func double_add(a, b)
    return add(a, b) gunaa 2
  khatam
  
  likho double_add(3, 4)  // 14
khatam
```

## Best Practices

1. **Use meaningful function names:**
   ```roman urdu
   func calculate_total(price, tax)  // Good
   func calc(p, t)                   // Unclear
   ```

2. **Keep functions focused:**
   - Each function should do one thing well
   - Avoid overly complex functions

3. **Document with comments:**
   ```roman urdu
   func sum_numbers(a, b)
     // Add two numbers and return result
     return a jodo b
   khatam
   ```

4. **Use consistent parameter names:**
   ```roman urdu
   func calculate(num1, num2)
     return num1 jodo num2
   khatam
   ```

## Limitations

Current version of cyberHunt functions:
- ✅ Support parameter passing
- ✅ Support return values
- ✅ Support local and global variables
- ❌ Do not support recursion (yet)
- ❌ Do not support default parameters
- ❌ Do not support variable arguments (*args)

## Error Messages

### Function Not Defined
```
NameError: Function 'foo' not defined
```
Solution: Make sure the function is defined before calling it.

### Wrong Number of Arguments
```
ValueError: Function 'add' expects 2 arguments, got 3
```
Solution: Call the function with the correct number of arguments.

### Variable Not Defined in Function
```
NameError: Variable 'undefined' not defined
```
Solution: Make sure all variables are initialized before use.

---

**Made with ❤️ for Urdu-speaking programmers**
