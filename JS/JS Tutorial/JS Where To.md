# JS Where To

## Contents

- [The `<script>` Tag](#the-script-tag)
- [JavaScript Functions and Events](#javascript-functions-and-events)
- [JavaScript in `<head>` or `<body>`](#javascript-in-head-or-body)
- [JavaScript in `<head>`](#javascript-in-head)
- [JavaScript in `<body>`](#javascript-in-body)
- [External JavaScript](#external-javascript)
- [External JavaScript Advantages](#external-javascript-advantages)
- [External References](#external-references)

## The `<script>` Tag

In HTML, JavaScript code is inserted between `<script>` and `</script>` tags.

```HTML
<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
</script>
```

## JavaScript Functions and Events

Functions can be called when an event occurs.

## JavaScript in `<head>` or `<body>`

A JavaScript code can be placed in the `<body>` or in the `<head>` section of an HTML page.

## JavaScript in `<head>`

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

## JavaScript in `<body>`

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

## External JavaScript

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

## External JavaScript Advantages

- It separates HTML and code
- It makes HTML and JavaScript easier to read and maintain
- Cached JavaScript files can speed up page loads

To add several scripts:

```HTML
<script src="myScript1.js"></script>
<script src="myScript2.js"></script>
```

## External References

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
