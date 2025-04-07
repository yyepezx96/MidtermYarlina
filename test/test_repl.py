import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest import mock
from io import StringIO
from repl import CalculatorREPL  # Import the REPL class from your repl.py file

# Mock the functions from other modules (calculator and history_manager)
@pytest.fixture
def mock_calculator():
    with mock.patch('repl.add', return_value=5), \
         mock.patch('repl.subtract', return_value=3), \
         mock.patch('repl.multiply', return_value=12), \
         mock.patch('repl.divide', return_value=2), \
         mock.patch('repl.add_to_history') as mock_add_to_history, \
         mock.patch('repl.show_history'), \
         mock.patch('repl.clear_history'), \
         mock.patch('repl.save_history'):
        yield mock_add_to_history

# Test the add command
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
@mock.patch('sys.stderr', new_callable=StringIO)
def test_do_add(mock_stdout, mock_stderr, mock_calculator):
    # Create an instance of the REPL class
    calculator_repl = CalculatorREPL()
   
    # Run the command (simulate user input for adding)
    calculator_repl.do_add("2 3")

    # Check if the output contains the correct result (stdout)
    print("Captured output:", mock_stdout.getvalue())  # For debugging purposes
    assert "5" in mock_stdout.getvalue()  # Ensure 5 is printed as the result

    # Check if the logger has logged the correct info (stderr)
    print("Captured error:", mock_stderr.getvalue())  # For debugging purposes
    assert "add command executed with result: 5" in mock_stderr.getvalue()

    # Check if add_to_history was called with the correct arguments
    mock_calculator.assert_called_with("add 2 3", 5)

# Test invalid input for add command
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
@mock.patch('sys.stderr', new_callable=StringIO)  # Capturing logs
def test_do_add_invalid_input(mock_stdout, mock_stderr, mock_calculator):
    # Create an instance of the REPL class
    calculator_repl = CalculatorREPL()

    # Run the command with invalid input (simulate user input)
    calculator_repl.do_add("two three")

    # Check if the output contains the invalid input message (stdout)
    print("Captured output:", mock_stdout.getvalue())  # For debugging purposes
    assert "Invalid input. Please enter numbers only." in mock_stdout.getvalue()

    # Check if the logger has logged the correct error (stderr)
    print("Captured error:", mock_stderr.getvalue())  # For debugging purposes
    assert "Invalid input for add command: two three" in mock_stderr.getvalue()

    # Check that add_to_history was not called with invalid input
    mock_calculator.assert_not_called()

    # Redirect stdout and stderr to the StringIO objects
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = captured_output
    calculator_repl.stderr = captured_error

    # Run the command (simulate user input for adding)
    calculator_repl.do_add("2 3")

    # Check if the output contains the correct result (stdout)
    print("Captured output:", captured_output.getvalue())
    assert "5" in captured_output.getvalue()

    # Check if the logger has logged the correct info (stderr)
    print("Captured error:", captured_error.getvalue())
    assert "add command executed with result: 5" in captured_error.getvalue()

    # Check if add_to_history was called with the correct arguments
    mock_calculator.assert_called_with("add 2 3", 5)

# Test invalid input for add command
def test_do_add_invalid(mock_calculator):
    # Capture both stdout and stderr
    captured_output = StringIO()
    captured_error = StringIO()

    # Redirect stdout and stderr to the StringIO objects
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = captured_output
    calculator_repl.stderr = captured_error

    # Run the command with invalid input
    calculator_repl.do_add("two three")

    # Check if the error message is shown (stdout)
    assert "Invalid input. Please enter numbers only." in captured_output.getvalue()

    # Check if the logger has logged the correct error (stderr)
    assert "Invalid input for add command: two three" in captured_error.getvalue()

# Test the divide command with division by zero
def test_do_divide_zero(mock_calculator):
    captured_output = StringIO()
    calculator_repl = CalculatorREPL()     
    calculator_repl.stdout = captured_output
    
    # Mock divide to raise a ZeroDivisionError
    with mock.patch('repl.divide', side_effect=ZeroDivisionError):
        calculator_repl.do_divide("5 0")
    
    # Check if the correct error message is shown for division by zero
    assert "Error: Cannot divide by zero." in captured_output.getvalue()

# Test history command
def test_do_history(mock_calculator):
    captured_output = StringIO()
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = captured_output
    
    # Run the history command
    calculator_repl.do_history("")
    
    # Check if the history command was logged
    assert "history command executed." in captured_output.getvalue()

# Test exit command
def test_do_exit(mock_calculator):
    captured_output = StringIO()
    calculator_repl = CalculatorREPL()  
    calculator_repl.stdout = captured_output
    
    # Run the exit command
    result = calculator_repl.do_exit("")
    
    # Check if the correct log message appears    
    assert "Goodbye!" in captured_output.getvalue()
    assert "Exiting the REPL." in captured_output.getvalue()  # Ensure the REPL exits gracefully
    assert result is True  # Test the save history command

# Test save history command
def test_do_save_history(mock_calculator):
    captured_output = StringIO()
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = captured_output
    
    # Run the save history command
    calculator_repl.do_save_history("history.csv")
    
    # Check if the history save command was logged
    assert "History saved to history.csv" in captured_output.getvalue()
