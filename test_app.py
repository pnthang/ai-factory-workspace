To write unit tests for `app.py`, we first need to understand the functionality that needs to be verified.

The `app.py` script:
1. Prints "Hello World" using `print()`.
2. Writes "Hello World" to a file named `hello.txt` using a context manager with the `open()` function and the `"w"` mode.

Now, let's write unit tests for these functionalities using Python's testing framework, `unittest`.

Create a new file named `app_test.py`:

```python
import unittest
from app import print_hello_world, write_to_hello_txt

class AppTest(unittest.TestCase):
    def test_print_hello_world(self):
        result = print_hello_world()
        self.assertEqual(result, "Hello World")

    def test_write_to_hello_txt(self):
        text = "Hello Again"
        expected_file_content = f"{text}\n"

        with open("hello.txt", "w") as file:
            file.write(write_to_hello_txt(text)))

        actual_file_content = file.read().strip()
        self.assertEqual(actual_file_content, expected_file_content)

if __name__ == "__main__":
    unittest.main()
```

Explanation of the `app_test.py` code:

1. Import the necessary modules: `unittest` for writing tests.
2. Create a class called `AppTest` that inherits from `unittest.TestCase`. This will help you write individual test methods.
3. Within the `AppTest` class, define two test methods:
   - `test_print_hello_world`: Checks if the function `print_hello_world()` correctly prints "Hello World".
   - `test_write_to_hello_txt`: Verifies that the function `write_to_hello_txt(text)`) writes the provided text to a file named `hello.txt`.
4. Finally, in the `if __name__ == "__main__":` block, call `unittest.main()` to run all tests.

Now, when you run the script `app.py` and then run the test suite `app_test.py`, it will verify if both print "Hello World" and write to the hello.txt file correctly.