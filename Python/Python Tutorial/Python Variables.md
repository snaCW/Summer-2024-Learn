# Pyhton Variables

## Contents

- [Casting](#casting)
- [Get the type](#get-the-type)
- [Case-Sensitive](#case-sensitive)
- [Variable Names](#variable-names)
- [Multi Words Variable Names](#multi-words-variable-names)
- [Many Values to Multiple Variables](#many-values-to-multiple-variables)
- [One Value to Multiple Variables](#one-value-to-multiple-variables)
- [Unpack a Collection](#unpack-a-collection)

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

## Variable Names

Rules for Python variables:

1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
4. A variable name cannot be any of the [Python keywords](../Python%20Reference/Python%20Keywords.md).

### [python_variable_names.py](Programs/python_variable_names.py) program

1. Create a new file and add these legal names:

    ``` Py
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"
    ```

2. Execute to see there is no problem. Now add these illegal names and execute again:

    ``` Py
    2myvar = "John" # Rule 2
    my-var = "John" # Rule 3
    my var = "John" # Rule 3
    ```

3. You can see there are errors.

## Multi Words Variable Names

There are several ways to make a multi word variable name more readable:

- **Camel Case**

    > Each word, except the first, starts with a capital letter

    ``` Py
    myVariableName = "John"
    ```

- **Pascal Case**

    > Each word starts with a capital letter

    ``` Py
    MyVariableName = "John"
    ```

- **Snake Case**

    > Each word is separated by an underscore character:

    ``` Py
    my_variable_name = "John"
    ```

## Many Values to Multiple Variables

You can assign values to multiple variables in one line.

### [python_assign_values](Programs/python_assign_multiple_values.py) program

1. Create a new file and add this code block:

    ``` Py
    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)
    ```

2. Execute. You can see the result.

## One Value to Multiple Variables

### [python_assign_multiple_variables](Programs/python_assign_multiple_variables.py) program

1. Create a new file and add this code block:

    ``` Py
    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)
    ```

2. Execute. You can see the result.

## Unpack a Collection

If you have a collection of values, you can assign them to variables. This is called **unpacking**.

### [python_assign_unpacking](Programs/python_assign_unpacking.py) program

1. Create a new file and add this code block:

    ``` Py
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)
    ```

2. Execute. You can see the result.
