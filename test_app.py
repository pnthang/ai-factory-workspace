```python
# test_app.py
import unittest

class TestApp(unittest.TestCase):
    def test_write_result(self):
        write_result = write_to_file(content, "hello.txt")
        self.assertEqual(write_result, None)
```
