# C++ Notes
Following along: https://www.youtube.com/watch?v=8jLOx1hD3_o&ab_channel=freeCodeCamp.org 

## C++ Dev Setup
- IDE: VSCode is good
- Compiler: software that takes written code and turns it into machine code
    - On mac/linux the compiler creates a binary that can run on the hardware
    - gcc is a good compiler for mac/linux
- Extensions: Install the C/C++ extension on VSCode
- Configure compiler in VSCode:
```json
{
	"version": "2.0.0",
	"tasks": [
		{
			"type": "cppbuild",
			"label": "C/C++: g++ build active file",
			"command": "/usr/bin/g++",
			"args": [
				"-fdiagnostics-color=always",
				"-g",
				"-std=c++20",
				"${workspaceFolder}/*",
				"-o",
				"${fileDirname}/${fileBasenameNoExtension}"
			],
			"options": {
				"cwd": "${fileDirname}"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": "build",
			"detail": "compiler: /usr/bin/g++"
		}
	]
}
```

## First Program
- The main function: the main function is the entry point for the C++ program.  It's the very first thing that will be run.
```cpp
#include <iostream>

int main(){

}
```
- Comments```cpp
#include <iostream>
// single line comment
/*
Multi
line
comment
*/
int main(){

}
```
- Errors and Warnings
    1. Compile-time errors -- compiler finds something like a syntax error that it freaks out about
    2. Runtime errors -- program compiles, but something goes wrong when running it
    3. Warnings -- program will technically compile, but the compiler might warn you it's not going to end well (e.g. dividing by 0)