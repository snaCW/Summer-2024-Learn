# JS Variables

## Contents

- [JavaScript Declaring](#javascript-declaring)
- [JavaScript Identifiers](#javascript-identifiers)
- [The Assignment Operator](#the-assignment-operator)
- [JavaScript Data Types](#javascript-data-types)
- [Declaring a JavaScript Variable](#declaring-a-javascript-variable)

## JavaScript Declaring

Variables can be declared in 4 ways:

- Automatically
- Using `var`
- Using `let`
- Using `const`

In the below example, `x`, `y`, and `z` are undeclared variables and are automatically declared.

``` JS
x = 5;
y = 6;
z = x + y;
```

> It is a good practice to always declare variables before use.

``` JS
var x = 5;
var y = 6;
var z = x + y;
```

``` JS
let x = 5;
let y = 6;
let z = x + y;
```

``` JS
const x = 5;
const y = 6;
const z = x + y;
```

``` JS
const x = 5;
const y = 6;
const z = x + y;
```

> When to use each?
>
> 1. Always declare variables
> 2. Always use `const` if the value should not be changed
> 3. Always use `const` if type should not be changed (Arrays and Objects)
> 4. Only use `let` if you can't use `const`
> 5. Only use `var` if you MUST support old browsers.

## JavaScript Identifiers

All variables must be identified with unique names.

The general rules for constructing names for variables are:

- Names can contain letters, digits, underscores, and dollar signs.
- Names cannot begin with digits.
- Names are case sensitive.
- Reversed words like keywords cannot be used.

## The Assignment Operator

The equal sign (`=`) is an "assignment" operator, not an "equal to" operator. The "equal to" operator is `==`.

## JavaScript Data Types

Strings are written inside double or single quotes. Numbers are written without quotes. If you put a number in quotes, it will be treated as a text string.

``` JS
const pi = 3.14;
let person = "John Doe";
let answer = 'Yes I am!';
```

## Declaring a JavaScript Variable

