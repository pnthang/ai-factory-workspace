To write unit tests for the `app.py` script, you'll need to use a testing framework like Python's built-in `unittest` module.

First, create a file named `app_test.py` in the same directory as your `app.py`. Then add the following code:

```python
import unittest
from app import print_hello_world, write_hello_to_txt

class AppTest(unittest.TestCase):
    def test_print_hello_world(self):
        result = print_hello_world()
        self.assertEqual(result, "Hello World")

    def test_write_hello_to_txt(self):
        output_file = "hello.txt"
        result = write_hello_to_txt(output_file)
        self.assertTrue(result, "Hello World written to hello.txt")
        self.assertFileExists(output_file)

    @classmethod
    def setup_class(cls):
        # You can add any setup required for your tests here

    @classmethod
    def teardown_class(cls):
        # You can add any cleanup required after your tests here


if __name__ == "__main__":
    unittest.main()
```

This code sets up a `unittest.TestCase` class named `AppTest` which contains two test methods:

1. `test_print_hello_world`: This method checks if the `print_hello_world()` function prints "Hello World" correctly.

2. `test_write_hello_to_txt`: This method checks if the `write_hello_to_txt(output_file))` function writes "Hello World" to a file named "hello.txt" correctly and that the file exists after writing.

Lastly, the script includes a setup and teardown class method to perform any necessary setup or cleanup tasks for your tests.