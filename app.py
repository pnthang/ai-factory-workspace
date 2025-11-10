Here is a simple Python script that prints "Hello World" to the console and writes it to a file named `hello.txt`:
```
# hello.py

print("Hello World")

with open("hello.txt", "w") as f:
    f.write("Hello World")
```
Let me explain what's going on:

* The first line, `print("Hello World")`, simply prints the string "Hello World" to the console.
* The second block of code uses a `with` statement to open a file named `hello.txt` in write mode (`"w"`). The file will be created if it doesn't already exist.
* Inside the `with` block, we use the `write()` method to write the string "Hello World" to the file.

To run this script, save it to a file called `hello.py`, then execute it using Python:
```
$ python hello.py
Hello World
```
After running the script, you should see the message "Hello World" printed to the console. Additionally, a file named `hello.txt` will be created in the same directory as your script, containing the string "Hello World".