# JS Statements

## Contents

- [JavaScript Statements](#javascript-statements)
- [Semicolons `;`](#semicolons-)
- [JavaScript White Space](#javascript-white-space)
- [JavaScript Line Length and Line Breaks](#javascript-line-length-and-line-breaks)
- [JavaScript Code Blocks](#javascript-code-blocks)

## JavaScript Statements

This statement tells to write "Holly Dolly." inside an HTML element with `id="demo"`.

``` JS
document.getElementById("demo").innerHTML = "Hello Dolly.";
```

## Semicolons `;`

Semicolons are used to indicate the end of each executable statement.

``` JS
let a, b, c;
a = 5;
b = 6;
c = a + b;
```

## JavaScript White Space

JavaScript ignore multiple spaces.

Here see two equivalent lines:

``` JS
let person = "Hege";
let person="Hege";
```

## JavaScript Line Length and Line Breaks

It is better to avoid code lines longer than 80 characters. You can always go to the next line.

``` JS
document.getElementById("demo").innerHTML =
"Hello Dolly!";
```

## JavaScript Code Blocks

Statements can be grouped inside curly brackets {...}.

``` JS
function myFunction() {
    document.getElementById("demo1").innerHTML = "Hello Dolly!";
    document.getElementById("demo2").innerHTML = "How are you?";
}
```

## JavaScript Keywords

| Keyword | Description |
| - | - |
| var | Declares a variable |
| let| Declares a block variable |
| const| Declares a block constant |
| if| Marks a block of statements to be executed on a condition |
| switch |Marks a block of statements to be executed in different cases |
| for | Marks a block of statements to be executed in a loop |
| function |Declares a function |
| return| Exits a function |
| try | Implements error handling to a block of statements |
