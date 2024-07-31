# JS Tutorial

## Contents
- [JS Introduction](#js-introduction)
    - [JavaScript Can Change HTML Content](#javascript-can-change-html-content)
    - [JavaScript Can Change HTML Attribute Values](#javascript-can-change-html-attribute-values)
    - [JavaScript Can Change HTML Styles (CSS)](#javascript-can-change-html-styles-css)
    - [JavaScript Can Hide HTML Elements](#javascript-can-hide-html-elements)
    - [JavaScript Can Show HTML Elements](#javascript-can-show-html-elements)

- [JS Where To](#js-where-to)
    - [The `<script>` Tag](#the-script-tag)
    - [JavaScript Functions and Events](#javascript-functions-and-events)
    - [JavaScript in `<head>` or `<body>`](#javascript-in-head-or-body)
    - [JavaScript in `<head>`](#javascript-in-head)
    - [JavaScript in `<body>`](#javascript-in-body)
    - [External JavaScript](#external-javascript)
    - [External JavaScript Advantages](#external-javascript-advantages)
    - [External References](#external-references)

- [JS Output](#js-output)
    - [JavaScript Display Possibilities](#javascript-display-possibilities)
    - [Using `.innerHTML`](#using-innerhtml)
    - [Using `document.write()`](#using-documentwrite)
    - [Using `window.alert()`](#using-windowalert)
    - [Using `console.log()`](#using-consolelog)
    - [JavaScript Print](#javascript-print)

## JS Introduction

### JavaScript Can Change HTML Content
Method `getElementById(string)` returns a reference to an HTML element. Since this is a reference, you can change the element content.
```JS
document.getElementById("demo").innerHTML = "Hello JavaScript";
document.getElementById("demo").innerHTML = 'Hello JavaScript';
```
As you can see, you can use both double and single quotes.

### JavaScript Can Change HTML Attribute Values
You can change the value of `scr` (source) attribute of an `<img>` tag.
```JS
document.getElementById('myImage').src='pic_bulbon.gif'; // Execute when turn on button clicked
document.getElementById('myImage').src='pic_bulboff.gif'; // Execute when turn off button clicked
```
As said, `getElementById(string)` returns a reference, so we used `.scr` to access its `scr` attribute and change the source image of `myImage` element.

### JavaScript Can Change HTML Styles (CSS)
```JS
document.getElementById("demo").style.fontSize = "35px";
```

### JavaScript Can Hide HTML Elements
```JS
document.getElementById("demo").style.display = "none";
```

### JavaScript Can Show HTML Elements
```JS
document.getElementById("demo").style.display = "block";
```

## JS Where To

### The `<script>` Tag
In HTML, JavaScript code is inserted between `<script>` and `</script>` tags.
```HTML
<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
</script>
```

### JavaScript Functions and Events
Functions can be called when an event occurs.

### JavaScript in `<head>` or `<body>`
A JavaScript code can be placed in the `<body>` or in the `<head>` section of an HTML page.

### JavaScript in `<head>`
As you can see, we wrote a function in `<head>` section.
```HTML
<!DOCTYPE html>
<html>
    <head>
        <script>
        function myFunction() {
            document.getElementById("demo").innerHTML = "Paragraph changed.";
        }
        </script>
    </head>

    <body>
        <h2>Demo JavaScript in Head</h2>

        <p id="demo">A Paragraph</p>
        <button type="button" onclick="myFunction()">Try it</button>
    </body>
</html>
```
We create a button with `onclick` event, executing the `myFunction()` code when the button is clicked.

### JavaScript in `<body>`
```HTML
<!DOCTYPE html>
<html>
    <body>

        <h2>Demo JavaScript in Body</h2>

        <p id="demo">A Paragraph</p>

        <button type="button" onclick="myFunction()">Try it</button>

        <script>
            function myFunction() {
                document.getElementById("demo").innerHTML = "Paragraph changed.";
            }
        </script>

    </body>
</html>
```
It's a good practice to place scripts at the bottom of the `<body>` element to improve the display speed.

### External JavaScript
Create a new file `myScript.js` and write this code:
```JS
function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}
```
This is an example for external JavaScript codes. You can include an external JavaScript file like below in the HTML file.
```HTML
<script src="myScript.js"></script>
```
External scripts can be placed both in `<head>` and `<body>`.

### External JavaScript Advantages
- It separates HTML and code
- It makes HTML and JavaScript easier to read and maintain
- Cached JavaScript files can speed up page loads

To add several scripts:
```HTML
<script src="myScript1.js"></script>
<script src="myScript2.js"></script>
```

### External References
In `<script>` tag, you can see the `src` attribute. The value of this attribute can be one of the followings:

- With a full URL (a full web address)
    ```HTML
    <script src="https://www.w3schools.com/js/myScript.js"></script>
    ```

- With a file path (like /js/)
    ```HTML
    <script src="/js/myScript.js"></script>
    ```

- Without any path
    ```HTML
    <script src="myScript.js"></script>
    ```

## JS Output

### JavaScript Display Possibilities
- Writing into an HTML element, using `.innerHTML`.
- Writing into the HTML output using `document.write()`.
- Writing into an alert box, using `window.alert()`.
- Writing into the browser console, using `console.log()`.

### Using `.innerHTML`
The `innerHTML` property defines the HTML content.
```HTML
<!DOCTYPE html>
<html>
    <body>
        <h1>My First Web Page</h1>
        <p>My First Paragraph</p>

        <p id="demo"></p>

        <script>
            document.getElementById("demo").innerHTML = 5 + 6;
        </script>
    </body>
</html>
```
So we can change the value of `"demo"` to 11.

### Using `document.write()`
This is a convenient way for testing purposes.
```HTML
<!DOCTYPE html>
<html>
    <body>
    <h1>My First Web Page</h1>
    <p>My first paragraph.</p>

    <script>
        document.write(5 + 6);
    </script>
    </body>
</html>
```
Using `document.write()` after an HTML document is loaded, will delete all existing HTML:
```HTML
<!DOCTYPE html>
<html>
    <body>
    <h1>My First Web Page</h1>
    <p>My first paragraph.</p>

    <button type="button" onclick="document.write(5 + 6)">Try it</button>
    </body>
</html>
```
The `document.write()` method should only be used for testing.

### Using `window.alert()`
```HTML
<!DOCTYPE html>
<html>
    <body>

    <h1>My First Web Page</h1>
    <p>My first paragraph.</p>

    <script>
        window.alert(5 + 6);
    </script>

    </body>
</html>
```
You can skip the `window` keyword.
```HTML
<script>
    alert(5 + 6);
</script>
```

### Using `console.log()`
For debugging purposes, you can call the `console.log()` method in the browser to display data.
```HTML
<!DOCTYPE html>
<html>
    <body>

    <script>
        console.log(5 + 6);
    </script>

    </body>
</html>
```

### JavaScript Print
You can send the current page to a printer.
```HTML
<!DOCTYPE html>
<html>
    <body>

    <button onclick="window.print()">Print this page</button>

    </body>
</html>
```