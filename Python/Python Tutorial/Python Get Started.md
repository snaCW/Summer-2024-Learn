# Python Get Started

## Contents

- [Python Install](#python-install)
- [Python Quickstart](#python-quickstart)
- [Python Version](#python-version)
- [The Python Command Line](#the-python-command-line)

## Python Install

To check if you have Python installed, search in the start bar for Python or run this command on the Command Line (cmd.exe):

``` Bash
python --version
```

You can download Python from <https://www.python.org/>

## Python Quickstart

The main way to execute a Python (.py) file is to use a text editor and write the code, and then use the Python interpreter.

### [helloworld.py](Programs/helloworld.py) program

> The Python file explained here is also available by clicking on the `helloworld.py` word for learning purposes. Please follow the steps by yourself first.
>
> From now on, the refrence file can be access through the provided links in each lesson.

1. Create a file with name `helloworld.py` in a desired folder.

2. Write this code inside the Python file and save it:

    ``` Py
    print("Hello World")
    ```

3. Right-click on the `helloworld.py` file and open the `Properties` window. Copy the `Location` and open the `terminal` (`cmd` for Windows).

    > The easier way to open the `terminal` in your desired folder is to click on the top `directory` bar and write `cmd` and then enter.

4. Enter the `terminal` and write this command:

    ``` Bash
    python {Location} helloworld.py
    ```

    > Do not type the {...} brackets. Just paste the `Location`.

Now you should have to see the `Hello World` message. This was your first Python program.

## Python Version

To find the Python version of your interpreter, you can import the `sys` module too.

### [python_version.py](Programs/python_version.py) program

1. Create a new file: `python_version.py`

2. Write this code:

    ``` Py
    import sys
    ```

3. After importing the `sys` module, you can get the `version` details. Add this line at the end of the file:

    ``` Py
    print(sys.version)
    ```

4. Run the file. You should be able to see the details.

## The Python Command Line

Creating a new file for only a short amount of code can be exhausting. You can use the **Python Command Line** to write the code directly.

1. Open the terminal in the desired path.

2. Write and run this command:

    ``` Bash
    python
    ```

3. You can see this messages:

    ``` Text
    Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

    > The result can be different if you have different Python version or different OS.

4. In the last line after `>>>` you can write your code:

    ``` Py
    print("Hello World")
    ```

5. The code immediately get executed:

    ``` Text
    Hello World
    ```

To quit the python command line, run this code:

``` Py
exit()
```
