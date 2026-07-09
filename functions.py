"""
cyberHunt Functions Module - Support for user-defined functions
Handles function definition, parameter passing, and return values
"""

from typing import Dict, List, Any, Optional

class Function:
    """Represents a user-defined function"""
    
    def __init__(self, name: str, parameters: List[str], body: List[Dict], return_stmt: Optional[Dict] = None):
        self.name = name
        self.parameters = parameters  # List of parameter names
        self.body = body  # List of statements
        self.return_stmt = return_stmt  # Optional return statement
    
    def __repr__(self):
        return f"Function({self.name}, params={self.parameters})"


class FunctionManager:
    """Manages function definitions and calls"""
    
    def __init__(self):
        self.functions: Dict[str, Function] = {}
        self.call_stack: List[Dict] = []
    
    def define_function(self, name: str, parameters: List[str], body: List[Dict], return_stmt: Optional[Dict] = None):
        """Define a new function"""
        if name in self.functions:
            raise NameError(f"Function '{name}' is already defined")
        
        self.functions[name] = Function(name, parameters, body, return_stmt)
    
    def get_function(self, name: str) -> Optional[Function]:
        """Get function by name"""
        return self.functions.get(name)
    
    def function_exists(self, name: str) -> bool:
        """Check if function exists"""
        return name in self.functions
    
    def push_scope(self, local_vars: Dict[str, Any]):
        """Push a new scope (for function calls)"""
        self.call_stack.append(local_vars)
    
    def pop_scope(self):
        """Pop current scope"""
        if self.call_stack:
            self.call_stack.pop()
    
    def get_current_scope(self) -> Dict[str, Any]:
        """Get current scope variables"""
        if self.call_stack:
            return self.call_stack[-1]
        return {}
    
    def list_functions(self) -> List[str]:
        """List all defined functions"""
        return list(self.functions.keys())
