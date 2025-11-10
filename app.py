Here is a simple Python script that prints "Hello World" and writes it to a file named `hello.txt`:
```
# hello.py
print("Hello World")
with open("hello.txt", "w") as f:
    f.write("Hello World\n")
```
Let me explain what each line does:

1. `print("Hello World")`: This is the classic "Hello World" print statement.
2. `with open("hello.txt", "w") as f:`: This opens a file named `hello.txt` in write mode (`"w"`). The `with` statement ensures that the file is properly closed when we're done with it, regardless of whether an exception is thrown or not.
3. `f.write("Hello World\n")`: This writes the string "Hello World\n" (note the newline character at the end) to the file.

To run this script, save it to a file named `hello.py` and then execute it using Python:
```
$ python hello.py
Hello World
```
After running the script, you should see the file `hello.txt` created in your current working directory with the contents "Hello World\n".