# Closure is a function that captures variables from its enclosing scope and retains access to them even after the outer function has finished executing.
from typing import Callable

def counter() -> Callable[[], int]:
    count = 0
    def increment()->int:
        # Use non local to use variable on the above level (use global if we need to use global veriable on the first level)
        nonlocal count
        count+=1
        return count
    
    return increment


call_count = counter()

print(call_count())
print(call_count())
print(call_count())


