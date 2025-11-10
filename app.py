Here is a simple Python program that prints "Hello World" to the console and also writes it to a file named `hello.txt`:
```
# hello.py
print("Hello World")
with open("hello.txt", "w") as f:
    f.write("Hello World")
```
Let me explain what's going on:

* The first line, `print("Hello World")`, simply prints the string "Hello World" to the console.
* The second line uses a context manager (`with` statement) to open a file named `hello.txt` in write mode (`"w"`). This ensures that the file is properly closed when we're done with it, even if an exception is thrown.
* Inside the `with` block, we use the `write()` method to write the string "Hello World" to the file.

To run this program, save it to a file named `hello.py` and then execute it using Python:
```
$ python hello.py
Hello World
```
After running the program, you should see that a new file named `hello.txt` has been created in your current working directory, containing the string "Hello World":
```
$ cat hello.txt
Hello World
```