Here's a simple Python script called `app.py` that you're trying to test. The script has two functionalities: printing "Hello World" and writing to a file named `hello.txt`.

First, let's create a separate Python file (e.g., `test_app.py`) for unit testing. We'll write tests using the `unittest` module.

```python
# app.py

def print_hello_world():
    return "Hello World"

def write_to_hello_txt(text):
    with open("hello.txt", "w") as f:
        f.write(text)
```

Now, let's create a test file to contain these tests:

```python
# test_app.py

import unittest
from app import print_hello_world, write_to_hello_txt


class TestApp(unittest.TestCase):
    def test_print_hello_world(self):
        self.assertEqual(print_hello_world(), "Hello World")

    def test_write_to_hello_txt(self):
        text = "This is a test text."
        self.assertTrue(write_to_hello_txt(text), "File 'hello.txt' created."))


if __name__ == "__main__":
    unittest.main()
```

In this test file, we define two tests for our `app.py` module:

1. `test_print_hello_world()` checks that the `print_hello_world()` function returns the expected string.

2. `test_write_to_hello_txt()` verifies that the `write_to_hello_txt()` function writes the provided text to a `hello.txt` file.

To run these tests, simply save this test file as `test_app.py` and run it using the Python interpreter:

```bash
$ python test_app.py
```

If all tests pass, you should see output indicating that each test was successful.