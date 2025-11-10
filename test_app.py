To write unit tests for `app.py`, we need to use a testing framework such as Python's built-in `unittest` module. Here's an example of how you can structure your unit tests:

1. Create a new file named `test_app.py` in the same directory as `app.py`.

2. Import necessary modules, including `unittest` and potentially some libraries from `app.py` (if they're used in testing).

3. Write the test cases for both printing "Hello World" and writing to `hello.txt`. Each test case should be a separate method within the `test_app.py` file.

Here's an example of how your `app.py` and `test_app.py` might look:

**app.py:**
```python
def hello_world():
    print("Hello World")

def write_to_hello_txt(text):
    with open("hello.txt", "w") as f:
        f.write(text)

# Example usage in main function or another context
hello_world()
write_to_hello_txt("Hello, hello!")
```

**test_app.py:**
```python
import unittest
from app import hello_world, write_to_hello_txt


class TestHelloWorld(unittest.TestCase):
    def test_print_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello World")


class TestWriteToHelloTxt(unittest.TestCase):
    def test_write_hello_text_to_file(self):
        text_to_write = "Hello, hello!"
        result = write_to_hello_txt(text_to_write)
        self.assertTrue(result, f"Hello, hello! written to 'hello.txt'")
```

In this example, `app.py` contains the functions for printing "Hello World" and writing to a file. `test_app.py` is where you define unit tests using the `unittest.TestCase` class.

The test cases for `TestHelloWorld` and `TestWriteToHelloTxt` verify that the functions in `app.py` perform their expected tasks correctly.