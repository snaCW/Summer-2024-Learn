# JS Syntax

## Contents

- [JavaScript Values](#javascript-values)
- [JavaScript Literals](#javascript-literals)
- [JavaScript Variables](#javascript-variables)
- [JavaScript Operators](#javascript-operators)
- [JavaScript Expressions](#javascript-expressions)
- [JavaScript Keywords](#javascript-keywords)
- [JavaScript Comments](#javascript-comments)
- [JavaScript Identifiers / Names](#javascript-identifiers--names)
- [JavaScript is Case Sensitive](#javascript-is-case-sensitive)
- [JavaScript and Camel Case](#javascript-and-camel-case)
- [JavaScript Character Set](#javascript-character-set)

## JavaScript Values

There are two types of values:

- Fixed values (Literals)
- Variable values (Variables)

## JavaScript Literals

The two most important literals are:

1. Numbers (with or without decimal)
2. Strings (within single or double quotes)

## JavaScript Variables

Variables are used to store data values. We use `var`, `let`, and `const` to declare variables.

``` JS
let x;
x = 6;
```

## JavaScript Operators

- Arithmetic operators (`+` `-` `*` `/`) to compute values

    ``` JS
    (5 + 6) * 10
    ```

- Assignment operator (`=`) to assign values

    ``` JS
    let x, y;
    x = 5;
    y = 6;
    ```

- And more...

## JavaScript Expressions

An expression is a combination of values, variables, and operators, which computes to a value. This computation is called evaluation.

``` JS
5 * 10 // Evaluates to 20
```

Expressions can contains variables or with various types:

``` JS
x * 10
"John" + " " + "Doe"
```

## JavaScript Keywords

We use keywords to identify the action to be performed.

- `let` tells the browser to create variables:

    ``` JS
    let x, y;
    x = 5 + 6;
    y = x * 10;
    ```

- `var` does the same in this example:

    ``` JS
    var x, y;
    x = 5 + 6;
    y = x * 10;
    ```

You will know more about `let` and `var` later.

## JavaScript Comments

Code after double slashes `//` or between `/*` and `*/` is treated as a comment.

Comments are ignored and not executed.

``` JS
let x = 5;   // I will be executed

// x = 6;   I will NOT be executed
```

## JavaScript Identifiers / Names

Identifiers are used to name variables and keywords, and functions.

The first character of a legal name can be one of these:

- A letter (A-Z or a-z)
- A dollar sign ($)
- An underscore (_)

Subsequent characters can be one of the above ones or a digit (0-9).

## JavaScript is Case Sensitive

Identifiers are case sensitive. All the below examples are different identifiers:

- `Lastname`
- `LastName`
- `lastname`
- `lastName`

So you can write a code like this:

``` JS
let lastname, lastName;
lastName = "Doe";
lastname = "Peterson";
```

Keywords are case sensitive too.

## JavaScript and Camel Case

There are different ways to join multiple words into one variable name:

- Hyphens: first-name, last-name
- Underscore: first_name, last_name
- Pascal Case: FirstName, LastName
- Camal Case: firstName, lastName

> Hyphens are not allowed in JavaScripts. JavaScript programmers tend to use camal case.

## JavaScript Character Set

JavaScript uses the Unicode character set.
