Here is a simple Python program that prints "Hello World" and writes it to a file named `hello.txt`:
```
# hello.py
print("Hello World")
with open("hello.txt", "w") as f:
    f.write("Hello World\n")
```
Let me explain what's happening:

1. The first line, `print("Hello World")`, simply prints the string "Hello World" to the console.
2. The second line uses a context manager (`with` statement) to open a file named `hello.txt` in write mode (`"w"`). This means that if the file doesn't exist, it will be created, and if it does exist, its contents will be truncated (i.e., deleted).
3. Inside the `with` block, we use the `write()` method to write the string "Hello World\n" to the file. The `\n` at the end adds a newline character, so that the output is properly formatted.

To run this program, save it to a file named `hello.py`, then execute it using Python:
```
$ python hello.py
Hello World
```
You should see "Hello World" printed to the console. Additionally, a new file named `hello.txt` will be created in the same directory, containing the string "Hello World\n".