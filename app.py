Here is a simple Python script that does what you asked:

```Python
# Print Hello World to the console
print("Hello World")

# Write Hello World to a file
with open("hello.txt", "w") as f:
    f.write("Hello World")
```

Let me explain what this code does:

- The first line, `print("Hello World")`, prints "Hello World" to the console.
- The second part of the script uses Python's built-in file handling capabilities to write "Hello World" to a file named "hello.txt".

Here are some important details about how it works:
- The `with` statement is used to open and automatically close the file. This ensures that the file is properly closed after we're done with it, even if an error occurs.
- The `"w"` argument means "write mode". If a file with this name already exists, its contents will be deleted before writing. If no such file exists, one will be created.

Save this script to a file (for example, `hello.py`), then run it using Python (e.g., `python hello.py`). You should see "Hello World" printed to the console and written to a file named "hello.txt".