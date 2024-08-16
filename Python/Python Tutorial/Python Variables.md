# Pyhton Variables

## Contents

- [Casting](#casting)
- [Get the type](#get-the-type)
- [Case-Sensitive](#case-sensitive)

## Casting

### [python_casting.py](Programs/python_casting.py) program

1. Create a Pyhton file: `python_casting.py`

2. Add this code:

    ``` Py
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0
    ```

You can cast the data to different types like this.

## Get the type

### [python_get_type.py](Programs/python_get_type.py) program

1. Copy the `python_casting.py` file you made already and rename it to `python_get_type.py`.

2. Add the code below to the end of the file. We use `type()` function to get the type.

    ``` Py
    print(type(x))
    print(type(y))
    print(type(z))
    ```

3. Execute. You can know understand both the casting and `type()` now.

## Single or Double Quotes?

### [python_string_quotes.py](Programs/python_string_quotes.py) program

1. Create a new file: `python_string_quotes.py`

2. Create two string variables with different quotes:

    ``` Py
    x = "John"
    y = 'John'
    ```

3. Add an `if` statement at the end of the file to check if `x` and `y` are equal or not:

    ``` Py
    if x == y:
        print("Both single and double quotes are okay.")
    ```

4. Execute. You can see the result.

## Case-Sensitive

### [python_case_sensitivity.py](Programs/python_string_quotes.py) program

1. Create a new file: `python_case_sensitivity.py`

2. Add this code:

    ``` Py
    a = 4
    a = 10
    print(a)
    ```

3. Execute. You can see the `a` is overwritten. Now add thid code:

    ``` Py
    A = 12
    print(a)
    ```

4. Execute. You can see the `A` did not overwrite the `a` because Python is case sensitive.

5. Now add this line at the end of the file and execute.

    ``` Py
    Print(A)
    ```

6. You can see the error: `NameError: name 'Print' is not defined. Did you mean: 'print'?`

So you should pay attention to use the right characters when coding.
