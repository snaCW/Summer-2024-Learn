# JS Introduction

## Contents

- [JavaScript Can Change HTML Content](#javascript-can-change-html-content)
- [JavaScript Can Change HTML Attribute Values](#javascript-can-change-html-attribute-values)
- [JavaScript Can Change HTML Styles (CSS)](#javascript-can-change-html-styles-css)
- [JavaScript Can Hide HTML Elements](#javascript-can-hide-html-elements)
- [JavaScript Can Show HTML Elements](#javascript-can-show-html-elements)

## JavaScript Can Change HTML Content

Method `getElementById(string)` returns a reference to an HTML element. Since this is a reference, you can change the element content.

```JS
document.getElementById("demo").innerHTML = "Hello JavaScript";
document.getElementById("demo").innerHTML = 'Hello JavaScript';
```

As you can see, you can use both double and single quotes.

## JavaScript Can Change HTML Attribute Values

You can change the value of `scr` (source) attribute of an `<img>` tag.

```JS
document.getElementById('myImage').src='pic_bulbon.gif'; // Execute when turn on button clicked
document.getElementById('myImage').src='pic_bulboff.gif'; // Execute when turn off button clicked
```

As said, `getElementById(string)` returns a reference, so we used `.scr` to access its `scr` attribute and change the source image of `myImage` element.

## JavaScript Can Change HTML Styles (CSS)

```JS
document.getElementById("demo").style.fontSize = "35px";
```

## JavaScript Can Hide HTML Elements

```JS
document.getElementById("demo").style.display = "none";
```

## JavaScript Can Show HTML Elements

```JS
document.getElementById("demo").style.display = "block";
```
