# MidtermYarlina: Python Calculator Application

## Description
A Python-based calculator application with a REPL interface, history management, and advanced logging features. This project uses design patterns and environment variables to manage settings.

## Features
- Basic arithmetic operations (Add, Subtract, Multiply, Divide)
- History management using Pandas
- Error handling for divide-by-zero and invalid inputs
- Logging with dynamic configuration through environment variables

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:yyepezx96/MidtermYarlina.git
   ```
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Testing:
   ```bash
   python3 repl.py
   ```
Once the application is running, you can interact with it via the command-line interface (REPL). Use the following commands to perform calculations:

add 3 2 to add numbers
subtract 5 3 to subtract numbers
multiply 6 7 to multiply numbers
divide 10 2 to divide numbers

To configure error use:             
   ```bash
   LOG_LEVEL=DEBUG python3 repl.py                                                          
   ``` 
