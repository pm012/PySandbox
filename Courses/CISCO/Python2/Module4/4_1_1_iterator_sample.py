'''In this example if Fib is implemented simply without inner class it will not be possible
to start iterating from scratch using the same object'''


class Fib:
    """
    The iterable class for Fibonacci numbers, using an inner iterator class.
    """
    def __init__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer")
        self.__n = n
        print(f"Fib iterable initialized (n={n})")

    # Define the iterator class as an inner class
    class _FibIterator: # Conventionally, use a leading underscore for inner/helper classes
        """
        The inner iterator class for Fib.
        This class holds the state of the Fibonacci sequence generation.
        """
        def __init__(self, n_limit):
            # n_limit is passed from the outer Fib instance
            self._n_limit = n_limit
            self._current_count = 0
            self._p1 = 1
            self._p2 = 1
            print(f"  _FibIterator initialized (limit={n_limit})") # Added indentation for clarity

        def __iter__(self):
            """
            An iterator's __iter__ method should always return itself.
            """
            print("  _FibIterator's __iter__ called: returning self")
            return self

        def __next__(self):
            """
            Generates the next Fibonacci number.
            """
            print(f"  _FibIterator's __next__ called (count={self._current_count}/{self._n_limit})")

            self._current_count += 1

            if self._current_count > self._n_limit:
                print("  _FibIterator: Limit reached, raising StopIteration")
                raise StopIteration
            elif self._current_count in [1, 2]:
                return 1
            else:
                ret = self._p1 + self._p2
                self._p1, self._p2 = self._p2, ret
                return ret

    def __iter__(self):
        """
        This method is called when an iteration is started on a Fib object.
        It creates and returns a NEW instance of the inner _FibIterator class.
        """
        print("Fib iterable's __iter__ called: returning a new _FibIterator")
        # Instantiate the inner class
        return Fib._FibIterator(self.__n) # Access the inner class via OuterClassName.InnerClassName

# --- Demonstration (same as before) ---

print("Creating a Fib iterable instance (f_sequence):")
f_sequence = Fib(10)

print("\n--- First Iteration ---")
for i in f_sequence:
    print(i)

print("\n--- Second Independent Iteration on the SAME f_sequence object ---")
for j in f_sequence:
    print(j)

print("\n--- Demonstrating independent iterators ---")
it1 = iter(f_sequence)
it2 = iter(f_sequence)

print("it1 next:", next(it1))
print("it2 next:", next(it2))
print("it1 next:", next(it1))
print("it1 next:", next(it1))
print("it2 next:", next(it2))