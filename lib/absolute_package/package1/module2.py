# Relative import example: import function1 from module1
from .module1 import function1

def call_module1():
    print("Calling module1 from module2 using relative import:")
    function1()

# This allows module2 to run directly with -m
if __name__ == "__main__":
    call_module1()
