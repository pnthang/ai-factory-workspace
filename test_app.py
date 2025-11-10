To write unit tests for the `app.py` script, you need to understand how the script works and what it is supposed to do.

Assuming that the `app.py` script has a function `print_hello_world()` which prints "Hello World" to the console and writes it to a file named "hello.txt", here's an example of unit tests for this scenario using Python's built-in testing library, `unittest`.

1. Create a new file called `app_test.py`.

2. Import the necessary modules:

```python
import unittest
from app import print_hello_world
```

3. Define the unit test class:

```python
class TestPrintHelloWorld(unittest.TestCase):
    def setUp(self):
        # Initialize variables or setup any required resources
        self.file_path = "hello.txt"
        self.console_output = "Hello World"

    def test_print_hello_world_to_console(self):
        # Test the function by calling it and checking its output
        result = print_hello_world()
        self.assertEqual(result, self.console_output)

    def test_write_hello_world_to_file(self):
        # Test that the function writes the expected content to the file
        result = print_hello_world(file_path=self.file_path))
        self.assertTrue(self.file_path in result and "Hello World" in result), f"Expected 'Hello World' written to {self.file_path}, but got: {result}")
```

4. Save the `app_test.py` file.

5. Run the tests:

```bash
python app_test.py
```

If all tests pass, you have successfully verified that your `app.py` script prints "Hello World" to the console and writes it to a file named "hello.txt".