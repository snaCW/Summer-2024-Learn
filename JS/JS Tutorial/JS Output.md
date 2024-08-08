# JS Output

## Contents

- [JavaScript Display Possibilities](#javascript-display-possibilities)
- [Using `.innerHTML`](#using-innerhtml)
- [Using `document.write()`](#using-documentwrite)
- [Using `window.alert()`](#using-windowalert)
- [Using `console.log()`](#using-consolelog)
- [JavaScript Print](#javascript-print)

## JavaScript Display Possibilities

- Writing into an HTML element, using `.innerHTML`.
- Writing into the HTML output using `document.write()`.
- Writing into an alert box, using `window.alert()`.
- Writing into the browser console, using `console.log()`.

## Using `.innerHTML`

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

## Using `document.write()`

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

## Using `window.alert()`

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

## Using `console.log()`

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

## JavaScript Print

You can send the current page to a printer.

```HTML
<!DOCTYPE html>
<html>
    <body>

    <button onclick="window.print()">Print this page</button>

    </body>
</html>
```
