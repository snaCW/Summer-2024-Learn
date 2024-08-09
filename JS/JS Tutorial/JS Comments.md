# JS Comments

## Contents

- [Single Line Comments](#single-line-comments)
- [Multi-line Comments](#multi-line-comments)
- [Using Comments to Prevent Execution](#using-comments-to-prevent-execution)

## Single Line Comments

Any text between `//` and the end of the line will be ignored to execute.

``` JS
// Change heading:
document.getElementById("myH").innerHTML = "My First Page";

// Change paragraph:
document.getElementById("myP").innerHTML = "My first paragraph.";
```

``` JS
let x = 5;      // Declare x, give it the value of 5
let y = x + 2;  // Declare y, give it the value of x + 2
```

## Multi-line Comments

Any text between `/*` and `*/` will be ignored to execute.

``` JS
/*
The code below will change
the heading with id = "myH"
and the paragraph with id = "myP"
in my web page:
*/
document.getElementById("myH").innerHTML = "My First Page";
document.getElementById("myP").innerHTML = "My first paragraph.";
```

Block comments (multi-line comments) are often used for formal documentaions.

## Using Comments to Prevent Execution

Add `//` in front of a code line to prevent the line to be executed.

``` JS
//document.getElementById("myH").innerHTML = "My First Page";
document.getElementById("myP").innerHTML = "My first paragraph.";
```

Or add `/*` and `*/` or prevent multiple lines to be executed.

``` JS
/*
document.getElementById("myH").innerHTML = "My First Page";
document.getElementById("myP").innerHTML = "My first paragraph.";
*/
```
