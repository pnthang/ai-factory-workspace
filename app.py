Here is a simple Python script that prints "Hello World" to the console and also writes it to a file named `hello.txt`:
```
# hello.py
print("Hello World")
with open("hello.txt", "w") as f:
    f.write("Hello World")
```
Let me explain what's going on:

1. The first line, `print("Hello World")`, simply prints the string "Hello World" to the console.
2. The `with` statement is used to open a file named `hello.txt` in write mode (`"w"`). The file is automatically closed when we're done with it, even if an error occurs.
3. Inside the `with` block, we use the `write()` method to write the string "Hello World" to the file.

To run this script, save it to a file named `hello.py` and then execute it using Python:
```
$ python hello.py
Hello World
```
You should see the output "Hello World" printed to the console. And if you look in the current directory, you should also see a file named `hello.txt` containing the same text.

Note: Make sure to run this script in a directory where you have write permissions!