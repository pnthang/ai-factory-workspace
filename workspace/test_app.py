Sure, here's an example of how you can write unit tests using the `unittest` module in Python:

**app.py** (the script to be tested)
```python
def print_hello_world():
    print("Hello World")

def write_to_file(text):
    with open('hello.txt', 'w') as f:
        f.write(text)

# Example usage of the functions
print_hello_world()
write_to_file("Hello, Hello. txt!")
```

**unit_tests.py** (the unit tests)
```python
import unittest
from app import print_hello_world, write_to_file

class AppTests(unittest.TestCase):
    def test_print_hello_world(self):
        result = print_hello_world()
        self.assertEqual(result, "Hello World")

    def test_write_to_file(self):
        text = "Hello, Hello again."
        result = write_to_file(text)
        self.assertTrue(result)  # Checks if the file was created or overwritten
        self.assertTrue(open('hello.txt', 'r').read(), equal=text))  # Checks if the content in the file matches the expected text

if __name__ == '__main__':
    unittest.main()
```

In this setup, we create a class `AppTests` that inherits from `unittest.TestCase`. This allows us to define test methods for each function in `app.py`.

The tests are:

1. `test_print_hello_world`: Checks if the `print_hello_world()` function correctly prints "Hello World" when called.

2. `test_write_to_file`: Checks if the `write_to_file(text)` function correctly writes the given text to a file named "hello.txt", either creating the file or overwriting it, and returns true indicating successful operation.

To run these tests, save both scripts in the same directory and then execute the command `python unit_tests.py` in the terminal. This will run all the test cases and display any failures or errors.