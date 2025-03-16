import cmd
import logging
from calculator import add, subtract, multiply, divide
from history_manager import add_to_history, show_history, clear_history, save_history #adding 2row

#set up logging
logger = logging.getLogger(__name__)

class CalculatorREPL(cmd.Cmd):
    prompt = '> '  # The prompt for the user

    def do_add(self, arg):
        "Add two numbers: add 2 3"
        try:
            nums = list(map(float, arg.split()))
            result = add(nums[0], nums[1])
            add_to_history(f"add {nums[0]}{nums[1]}", result) #add to history
            logger.info(f"add command executed with result: {result}") #log command
            print(result)
        except ValueError:
            logger.error(f"Invalid input for add command: {arg}") #logs error
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")  # Log unexpected errors
            print(f"Unexpected error: {e}")

    def do_subtract(self, arg):
        "Subtract two numbers: subtract 5 2"
        try:
            nums = list(map(float, arg.split()))
            result = subtract(nums[0], nums [1])
            add_to_history(f"subtract {nums[0]} {nums[1]}", result)
            logger.info(f"subtract command executed with result: {result}")  
            print(result)
        except ValueError:
            logger.error(f"Invalid input for subtract command: {arg}")
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error: {e}")

    def do_multiply(self, arg):
        "Multiply two numbers: multiply 3 4"
        try:
            nums = list(map(float, arg.split()))
            result = multiply(nums[0], nums[1])
            add_to_history(f"multiply {nums[0]} {nums[1]}", result)            
            logger.info(f"multiply command executed with result: {result}")
            print(result)
        except ValueError:
           logger.error(f"Invalid input for multiply command: {arg}") 
           print("Invalid input. Please enter numbers only.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error: {e}")


    def do_divide(self, arg):
        "Divide two numbers: divide 6 2"
        try:
            nums = list(map(float, arg.split()))
            result = divide(nums[0], nums[1])
            add_to_history(f"divide {nums[0]} {nums[1]}", result)            
            logger.info(f"divide command executed with result: {result}")            
            print(result)
        except ValueError:
          logger.error(f"Invalid input for divide command: {arg}")  
          print("Invalid input. Please enter numbers only.")
        except ZeroDivisionError:
            logger.warning("Attempted division by zero!") #logerror dividison
            print("Error: Cannot divide by zero.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error: {e}")


    # For Historyy Management Function Coding
    def do_history(self, arg):
        "Show the calculation history."
        show_history()  # Shows all history operations
        logger.info("history command executed.")  # Log the history command

    def do_clear_history(self, arg):
        "Clear the calculation history."
        clear_history()  # Clears the history
        logger.info("History cleared.")  # Log history clearance        
        print("History cleared.")

    def do_save_history(self, arg):
        "Save the history to a file: save_history history.csv"
        save_history(arg)  # Save the history to a CSV file
        logger.info(f"History saved to {arg}")  # Log history saving

    def do_exit(self, arg):
        "Exit the REPL."
        print("Goodbye!")
        logger.info("Exiting the REPL.")  # Log exit command        
        return True  # Exit the REPL

if __name__ == '__main__':
    CalculatorREPL().cmdloop() #to loop

