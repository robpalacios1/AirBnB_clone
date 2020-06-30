<p align="center"><img src= "https://imgur.com/cxhxj5h"/></p>
<p align="center"><img src= "https://media.itsnicethat.com/original_images/563b97a87fa44cff9d001760.gif" width="600" height="400"/></p>


# AirBnB clone - The console :ab::rocket:
The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website. 

This project was created to **Holberton School.**

## Table of contents :clipboard:

 - [Description](https://github.com/davixcky/simple_shell#description-triangular_ruler)
 - [Installation](https://github.com/davixcky/simple_shell#installation-floppy_disk)
 - [Usage](https://github.com/davixcky/simple_shell#usage-hammer)
 - [Example](https://github.com/davixcky/simple_shell#example-computer)
 - [File Structure](https://github.com/davixcky/simple_shell#file-structure-file_folder)

## Description :triangular_ruler:

This is a shell written in `c` for final project of `Holberton School`. `k_shell` its based on `sh` and support just the main functionalities.

The project structure can't have source inside directories, because the only way for compile in this case is `gcc -Wall -Werror -Wextra -pedantic *.c -o hsh`

This shell receive the name of `K-shell`, because represent our region, `la costa`. `K-shell` stands for `Kayman` that means `caiman` the animal of this region, so represent our culture and our live style. And the other part, `shell` is just the postfix

## Installation :floppy_disk:

### Requirements
 - Python 3.4
 - PEP 8

### Steps
 - `git clone https://github.com/davixcky/simple_shell.git shell`
 - `cd shell`
 - `gcc -Wall -Werror -Wextra -pedantic *.c -o hsh`
 - Enjoy it

## Usage :hammer:

*k_shell* supports two modes `interactive` and `non interactive`.

### Basic usage
`./hsh`

### Interactive

 - `./hsh` and then type the commands that you want to execute
 - You can type a command and the prompt appear show again

### Non interactive 

 - `echo "command" | ./hsh`, command is the command that you want to execute
 - Each time that you execute a command, the shell close

## Example :computer:

### Modes

#### Non-interactive
*Command*
```
echo "/bin/ls" | ./hsh
```
*Output*
```
AUTHORS     commands.h     error.c  execute.c  hsh     permissions.c  printers_err.c  README.md  start.c  text.h          utils_text2.c
commands.c  environment.c  error.h  general.h  main.c  printers.c     printers_out.c  shell.h    text.c   tokenization.c  utils_text.c
```
<hr>

#### Interactive
*Command*
```
./hsh
```
Then the prompt appear, so you can type in the command line, and press return
**Ex** - `/bin/ls`

*Output*
```
AUTHORS     commands.h     error.c  execute.c  hsh     permissions.c  printers_err.c  README.md  start.c  text.h          utils_text2.c
commands.c  environment.c  error.h  general.h  main.c  printers.c     printers_out.c  shell.h    text.c   tokenization.c  utils_text.c
```

## File Structure :file_folder:

<p align="center"> 
<img src = "https://imgur.com/hImZBUL.jpg" />
</p>

## Contributors  
[@Hugo Santiago - Github](https://github.com/hfsantiago) - [@Roberto Palacios - Github](https://github.com/robpalacios1) 
