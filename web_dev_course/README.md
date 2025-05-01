# Web Dev Course
Examples and notes from The Complete Full-Stack Web Development Bootcamp course on Udemy

## CSS
### What is CSS?
- Cascading Style Sheets
- Uses Style Sheet language
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
    
