CS333 - Project 2 - README
Parth Parth
02/24/2022

└── Project 2
    ├── README.txt
    ├── clite.yy
    ├── clite.yy.c
    ├── encode.yy
    ├── encode.yy.c
    ├── helloWorld.r
    ├── hello_world.R
    ├── helloworld.py
    ├── html.yy
    ├── html.yy.c
    ├── linescharsvowels.yy
    ├── linescharsvowels.yy.c
    └── moreComplicated.py

Config:
Ubuntu 20.04.3 LTS using WSL on Windows 11 - gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0

To run the programs:
flex FILENAME.yy
gcc -o repl lex.yy.c -ll
./repl

Tasks:

The first task is completed in encode.yy, the second in linescharsvowels.yy, third in html.yy and the final task is in clite.yy.
encode.yy does not read a file and requires inputs in the command line, but the other three programs take files as input.
No bugs were found in any of the files, but they most likely exist.

Extension 1: For the Clite parser, I have individually impelmented the functionality to ignore comments.
Extension 2: For the HTML parser, I have individually impelmented the functionality to replace &gt; with > and &lt; with <.
