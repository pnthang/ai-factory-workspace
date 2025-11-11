Here is a simple Python script that does what you asked:

```
# Print 'Hello World' to the console
print("Hello World")

# Open a file named 'hello.txt' in write mode
with open('hello.txt', 'w') as f:
    # Write 'Hello World' to the file
    f.write("Hello World")
```

Let me explain what this script does:

1. The first line, `print("Hello World")`, prints the string "Hello World" to the console.
2. The second part of the script opens a file named "hello.txt" in write mode (`'w'`). This will create the file if it doesn't already exist, or overwrite it if it does.
3. Inside the `with` block, we use the `write()` method to write the string "Hello World" to the file.

To run this script, save it to a file with a `.py` extension (e.g., `hello.py`) and then run it using Python (e.g., `python hello.py`). This will print "Hello World" to the console and create a file named "hello.txt" containing the same text.