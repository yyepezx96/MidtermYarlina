import cmd
from calculator import add, subtract, multiply, divide

class CalculatorREPL(cmd.Cmd):
    prompt = '> '  # The prompt for the user

    def do_add(self, arg):
        "Add two numbers: add 2 3"
        try:
            nums = list(map(float, arg.split()))
            print(add(nums[0], nums[1]))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def do_subtract(self, arg):
        "Subtract two numbers: subtract 5 2"
        try:
            nums = list(map(float, arg.split()))
            print(subtract(nums[0], nums[1]))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def do_multiply(self, arg):
        "Multiply two numbers: multiply 3 4"
        try:
            nums = list(map(float, arg.split()))
            print(multiply(nums[0], nums[1]))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def do_divide(self, arg):
        "Divide two numbers: divide 6 2"
        try:
            nums = list(map(float, arg.split()))
            print(divide(nums[0], nums[1]))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def do_exit(self, arg):
        "Exit the REPL."
        print("Goodbye!")
        return True  # Exit the REPL

if __name__ == '__main__':
    CalculatorREPL().cmdloop()

