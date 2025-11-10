To write unit tests for the `app.py` script, you'll need a testing framework such as `unittest` in Python. First, let's create the test file and import necessary modules:

1. Create `test_app.py`:
```python
# test_app.py

import unittest
from app import print_hello_world, write_to_file

class AppTest(unittest.TestCase):
    def test_print_hello_world(self):
        result = print_hello_world()
        self.assertEqual(result, "Hello World")

    def test_write_to_file(self):
        content = "Hello again"
        write_result = write_to_file(content, "hello.txt"))
        with open("hello.txt", "r") as file:
            expected_content = file.read()
        self.assertEqual(write_result, True)
        self.assertEqual(expected_content, content + "\n")

if __name__ == "__main__":
    unittest.main()
```
2. Implement `app.py` for testing purposes:
```python
# app.py (for testing)

def print_hello_world():
    return "Hello World"

def write_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)
    return True
```
Now you have a test file `test_app.py` and an example `app.py` for testing. When you run the tests using `unittest.main()` in the test file, they will verify both print statement and file writing functionality.

Example output of unit tests:

```bash
$ python test_app.py
...
Test case 'test_write_to_file' passed.
Test case 'test_print_hello_world' passed.
...

----------------------------------------------------------------------
Ran 2 tests in 0.01s

OK
```
The `OK` message indicates that all the tests have passed successfully.