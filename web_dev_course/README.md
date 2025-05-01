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