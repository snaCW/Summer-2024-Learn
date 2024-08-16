# Python Syntax

## Contents

- [Python Indentation](#python-indentation)
- [Python Variables](#python-variables)
- [Comments](#comments)

## Python Indentation

Identation refers to the spaces at the beginning of a code line.

Python uses identation to show a code block.

### [python_identation](Programs/python_identation.py) program

1. Create a new Python file: `python_identation.py`

2. Write an `if` statement:

    ``` Py
    if 5 > 2:
    ```

3. In the next line, it is expected to write the code to get execute if the `if` statement becomes `true`:

    ``` Py
    print("Five is greater than two")
    ```

    > Use no identations!

4. Execute the program. You should see this error:

    ``` Text
      File "{PATH}\python_identaion.py", line 2
    print("Five is greater than two!")
    ^
    IndentationError: expected an indented block after 'if' statement on line 1
    ```

    - `{PATH}` refers to the location of the containing folder.
    - `line 2` shows which line has an error.
    - `print("Five is greater than two!")` shows the mentioned line.
    - `^` indicated where the error has found in the line.
    - `IndentationError: expected an indented block after 'if' statement on line 1` explains the error. It says we need to identate the line after `if` statement.

5. Identate the line. The result should be like this:

    ``` Py
    if 5 > 2:
        print("Five is greater than two")
    ```

6. Execute. You should see no problems.

The number of spaces is up to you, but it should be at least one. The common space count is 4, that automatically is inserted if you use the `Tab` key on Visual Studio Code.

However, you have to use the **same** number of spaces in the same code block.

### [python_unexpected_identation](Programs/python_unexpected_identation.py) program

1. Copy the `python_identation.py` file that you created and rename it to `python_unexpected_identation.py`

2. Add this line at the end of the file with no identations:

    ``` Py
    print("Five is greater than two!")
    ```

3. Execute. You can see the program works. Now identate the last line with one space and execute again.

    ``` Text
    IndentationError: unindent does not match any outer indentation level
    ```

    > The `if` statement has **no spaces** and the code block inside has **four spaces**. Python tries to see this new line is a same code block of the `if` statement or it is in the `if` statement.
    >
    > However it can't decide because the line has **one spaces**.

4. Add four more spaces to the point the last line has five spaces. Execute.

    ``` Text
    IndentationError: unexpected indent
    ```

You can see the indent is very important in Python.

Code blocks should have more spaces than the outer code block. `if` statements in the examples had zero spaces, so the code inside should have at least one.

## Python Variables

In Python, variables are created when you assign a value to them.

### [python_variables.py](Programs/python_variables.py) program

1. Create a Pyhton file: `python_variables.py`

2. Write this code:

    ``` Py
    x = 5
    y = "John"
    ```

    > You have created two variables easily!

3. Use `print` to see the value of the variables, and then execute the program:

    ``` Py
    print(x)
    print(y)
    ```

4. Add this code block to the end of the file and execute again:

    ``` Py
    a = 100
    print(a)
    a = "Hello"
    print(a)
    ```

    > We easily changed the type of the variable `x` from *integer* to *string*.

5. You can see a variable can change its type.

## Comments

Comments start with `#`.

### [python_comments.py](Programs/python_comments.py) program

1. Create a Python file: `python_comments.py`

2. Write this code:

    ``` Py
    print("Hello World")
    ```

3. Add this line before the existing code:

    ``` Py
    # This is a comment
    ```

4. Execute. You can see the comments is not executed.

5. Now add `#` before the second line. The result should be like this:

    ``` Py
    # This is a comment
    # print("Hello World")
    ```

6. Execute. You can see the second line did not executed.

You can use comments to:

- Explain the code or gives a documentation.
- Disable some codes in order to debug the code.
