# Python Data Types

## Contents

- [Built-in Data Types](#built-in-data-types)
- [Getting the Data Type](#getting-the-data-type)
- [Setting the Data Type](#setting-the-data-type)
- [Setting the Specific Data Type](#setting-the-specific-data-type)

## Built-in Data Types

Python has the following built-in data types:

|   Category   |              Type(s)               |
| ------------ | ---------------------------------- |
| Text         | `str`                              |
| Numeric      | `int`, `float`, `complex`          |
| Sequence     | `list`, `tuple`, `range`           |
| Mapping Type | `dict`                             |
| Set Types    | `set`, `frozenset`                 |
| Boolean      | `bool`                             |
| Binary       | `bytes`, `bytearray`, `memoryview` |
| None         | `NoneType`                         |

## Getting the Data Type

You can get the type of a variable using `type()` function.

### [python_type_function](Programs/python_type_function.py)

1. Print the data type of variable x:

    ``` Py
    x = 5
    print(type(x))
    ```

2. You can try other values for `x` too.

## Setting the Data Type

In Python, the data type is set when you assign a value to a variable. You can try the examples below in the [python_set_type](Programs/python_set_type.py) program too. You just need to execute it directly.

|                     Example                    | Data Type  |
| ---------------------------------------------- | ---------- |
| `x = "Hello World"`                            | str        |
| `x = 20`                                       | int        |
| `x = 20.5`                                     | float      |
| `x = 1j`                                       | complex    |
| `x = ["apple", "banana", "cherry"]`            | list       |
| `x = ("apple", "banana", "cherry")`            | tuple      |
| `x = range(6)`                                 | range      |
| `x = {"name" : "John", "age" : 36}`            | dict       |
| `x = {"apple", "banana", "cherry"}`            | set        |
| `x = frozenset({"apple", "banana", "cherry"})` | frozenset  |
| `x = True`                                     | bool       |
| `x = b"Hello"`                                 | bytes      |
| `x = bytearray(5)`                             | bytearray  |
| `x = memoryview(bytes(5))`                     | memoryview |
| `x = None`                                     | NoneType   |

## Setting the Specific Data Type

To specify the data type you are going to use, use the proper constructor.

|                     Example                    | Data Type  |
| ---------------------------------------------- | ---------- |
| `x = str("Hello World")`                       | str        |
| `x = int(20)`                                  | int        |
| `x = float(20.5)`                              | float      |
| `x = complex(1j)`                              | complex    |
| `x = list(("apple", "banana", "cherry"))`      | list       |
| `x = tuple(("apple", "banana", "cherry"))`     | tuple      |
| `x = range(6)`                                 | range      |
| `x = dict("name" = "John", "age" = 36)`        | dict       |
| `x = set(("apple", "banana", "cherry"))`       | set        |
| `x = frozenset(("apple", "banana", "cherry"))` | frozenset  |
| `x = bool(5)`                                  | bool       |
| `x = bytes(5)`                                 | bytes      |
| `x = bytearray(5)`                             | bytearray  |
| `x = memoryview(bytes(5))`                     | memoryview |
