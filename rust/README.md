# Rust Notes
Installing Rust is pretty simply done using rustup: https://www.rust-lang.
Run the provided command in a terminal.  Stick with the standard install, and once it's done open a new terminal.  Type in the command `cargo` which is the Rust package manager to check it worked.

# Rust Projects
- ```bash
cargo new <project-name>
```
This creates a directory with some boilerplate for a Rust project.
It includes a "Hello World" file as well.
- ```bash
cargo run
```
Compiles and runs the project.  `-q` flag can be added to forgo the debug information.

# Rust Fundamentals
- `main()`
The main function in Rust is called automatically when the program is run.
An example of a simple "Hello World":
```rust
fn main(){
    println!("Hello World!");
}
```
- Syntax
    - `!` is for a Rust macro
    - Strings have double quotes ""
    - Chars have single quotes '' (A char is a single character only)
    - Struct: An OOP feature, and like a class in other languages.
    - Binding: A Rust "variable"
    - Type annotations: Small notes in the code that make it explicit what type is being used.  This is information the compiler can use to right away know what type is being referred to and not have any slowdowns inferring or searching. `let deck: Deck = `
    - Struct literal -- An instance of a struct `Deck {cards: vec![] }`
    ```rust
    let deck: Deck = Deck {cards: vec![] },
    ```
    - Struct attributes: A way to tell the compiler to automatically include a set of functions into a struct: `#[derive(Debug)]` tells the compiler, "Put all of the debug stuff into this struct"
- Data
    - Vector: a dynamic-sized data container
    - Array: a fixed data container