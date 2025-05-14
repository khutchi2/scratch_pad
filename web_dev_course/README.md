# Web Dev Course
Examples and notes from The Complete Full-Stack Web Development Bootcamp course on Udemy

## CSS
### What is CSS?
- Cascading Style Sheets
- Uses Style Sheet language

### Where can it be incorporated?
- 3 ways to add: Inline, Internal, External
    - Inline
        - Goes right into the same line as an html element
        ```html
        <html style="background: blue">
        </html>
        ```
        - `"property: value"`
        - Generally for testing, specific sections, or just for 1 element
    - Internal
        - Done using the `<style></style>` tag
        ```html
        <style>
            html{
                background: red
            }
        </style>
        ```
        - Good for applying to one HTML document only
    - External
        - Done by linking to a .css file
        ```html
        <html>
            <head>
                <link rel="stylesheet" href="./styles.css"/>
            </head>
        </html>
        ```
        - In the link tag, `rel` is the relationship, i.e. what role does this play?, and the `href` which points to the file itself
        - Most common, most modular way to use CSS
### Selectors
- A CSS Selector is the text from an HTML tag and selects the elements to apply the styling to.  For example, below `h1` is the selector:
    ```css
        h1{
            color: red
        }
    ```
- Types of Selectors
    - Element: like the `h1` selector above.  Applies styling to **all** elements with that tag.
    - Class: formatted as `.class` such as `.red-heading`.  A class is an attribute that can be added to any HTML element like this 
    ```html
    <h2 class="red-text"> Heading! </h2>
    <h3> Another heading </h3>
    <p class="red-text"> Stuff and junk </p>
    ```
    we can make a class selector to apply the styling to anything with that class:
    ```css
    .red-text{
        color: red
    }
    ```
    - ID Selector: uses the format `#ID`
    ```css
    #main{
        color: blue
    }
    ```
    It's similar to a class selector in that it applies to only elements with a particular ID.  The nuance is that an ID attribute should only apply to ONE element in the entire HTML document.  So the ID selector is for targeted element styling.
    - Attribute: there are plenty of HTML tags that have attributes.  You can select based on those extant attributes instead of having to tag them with a class.  This is formatted as `tag[attribute]` For example:
    ```html
    # HTML
    <p draggable="True"> Drag me! </p>
    <p> Don't drag me </p>
    <p> Nor me </p>
    ```
    ```css
    # CSS
    p[draggable]{
        color: red
    }
    ```
    You can even drill down to specific attribute values
    ```css
    # CSS
    p[draggable="True"]{
        color: red
    }
    ```
    - Universal Selector: The Universal selector is just a "*"
    ```css
    * {
        color: red
    }
    ```
    It applies the styling to all of the things where the style sheet is active.
### Properties
- CSS Properties
    - Colors: can be defined by name, or by hex-code e.g. #FAF8F1
    - Fonts: color, weight, size, family can all be defined
        - Size: `em` and `rem` are relative units.  `Xem` is `X` multiples of the parent element styling size, and `Xrem` is `X` multiples of the root element styling size.  For example:
        ```html
        <body> 20px
            <h1> Stuff and Junk </h1> 2em
        </body>
        ```
        would have `h1` set to `40px`.  The parent element is the element one layer up.  The root element is the most parental parent element (usually the <html> element)
### CSS Inspection
- Open up inspector in web browser
- There's a style tab that shows you CSS styling
### Box Model: Margin, Padding, Border
- Border: Grows out from your element (i.e. if you have a 30x30px box and put a 10x10px border on it, it's now 40x40px overall).  Can also tack on styling, that is, create the full border, then modify the top.
```css
border: 10px solid black;
    border-top: 0px;
```
Can also specify using `border-width` which goes clockwise from the top of the box at 1:
```css
border: 30px solid black;
    border-width: 10px 0px 20px 40px;
```
This box will have a thinner top border, no right border, a medium bottom border, and a thicker left border.  Both padding and margin also follow this convention of 4 values going around each side.
- Padding: Provides a buffer between a border element and enclosed elements i.e. pushes a border outward from the inner element by a specified amount
- Margin: Adds spacing outside of a border between it and other elements
#### <div></div>
The HTML division <div> element allows you to group together HTML elements into boxes.  The boxes in question are CSS boxes.