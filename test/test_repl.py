import pytest
import sys
import os
from unittest import mock
from io import StringIO
from repl import CalculatorREPL  # Import the REPL class from your repl.py file

# Mock the functions from other modules (calculator and history_manager)
@pytest.fixture
def mock_calculator():
    with mock.patch('repl.add', return_value=5) as mock_add, \
         mock.patch('repl.subtract', return_value=3) as mock_subtract, \
         mock.patch('repl.multiply', return_value=12) as mock_multiply, \
         mock.patch('repl.divide', return_value=2) as mock_divide, \
         mock.patch('repl.add_to_history') as mock_add_to_history, \
         mock.patch('repl.show_history'), \
         mock.patch('repl.clear_history'), \
         mock.patch('repl.save_history'):
        yield mock_add_to_history  # Yield the mock_add_to_history so it can be asserted


# Test the add command
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
@mock.patch('sys.stderr', new_callable=StringIO)  # Capturing error logs
def test_do_add(mock_stdout, mock_stderr, mock_calculator):
    # Create an instance of the REPL class
    calculator_repl = CalculatorREPL()

    # Run the command (simulate user input for adding)
    calculator_repl.do_add("2 3")

    # Check the captured output and error logs
    captured_output = mock_stdout.getvalue().strip()
    captured_error = mock_stderr.getvalue().strip()

    print("Captured output:", captured_output)  # For debugging purposes
    print("Captured error:", captured_error)    # For debugging purposes

    # Assertions for output and logs
    assert "5" in captured_output  # Should print "5"
    assert "add command executed with result: 5" in captured_error  # Log info

    # Verify that add_to_history was called
    mock_calculator.assert_called_with("add 2 3", 5)


# Test invalid input for add command
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
@mock.patch('sys.stderr', new_callable=StringIO)  # Capturing error logs
def test_do_add_invalid_input(mock_stdout, mock_stderr, mock_calculator):
    # Create an instance of the REPL class
    calculator_repl = CalculatorREPL()

    # Run the command with invalid input (simulate user input)
    calculator_repl.do_add("two three")

    # Check the captured output and error logs
    captured_output = mock_stdout.getvalue().strip()
    captured_error = mock_stderr.getvalue().strip()

    print("Captured output:", captured_output)  # For debugging purposes
    print("Captured error:", captured_error)    # For debugging purposes

    # Assertions for error messages
    assert "Invalid input. Please enter numbers only." in captured_output
    assert "Invalid input for add command: two three" in captured_error

    # Verify that add_to_history was not called
    mock_calculator.assert_not_called()


# Test the divide command with division by zero
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
def test_do_divide_zero(mock_stdout):
    calculator_repl = CalculatorREPL()

    # Mock divide to raise a ZeroDivisionError
    with mock.patch('repl.divide', side_effect=ZeroDivisionError):
        calculator_repl.do_divide("5 0")

    # Check if the correct error message is shown for division by zero
    captured_output = mock_stdout.getvalue().strip()
    assert "Error: Cannot divide by zero." in captured_output


# Test history command
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
def test_do_history(mock_stdout):
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = mock_stdout  # Capture output

    # Run the history command
    calculator_repl.do_history("")

    # Check if the history command was logged
    captured_output = mock_stdout.getvalue().strip()
    assert "history command executed." in captured_output


# Test exit command
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
def test_do_exit(mock_stdout):
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = mock_stdout  # Capture output

    # Run the exit command
    result = calculator_repl.do_exit("")

    # Check if the correct log message appears
    captured_output = mock_stdout.getvalue().strip()
    assert "Goodbye!" in captured_output
    assert "Exiting the REPL." in captured_output  # Ensure the REPL exits gracefully
    assert result is True  # Test the save history command


# Test save history command
@mock.patch('sys.stdout', new_callable=StringIO)  # Capturing printed output
def test_do_save_history(mock_stdout):
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = mock_stdout  # Capture output

    # Run the save history command
    calculator_repl.do_save_history("history.csv")

    # Check if the history save command was logged
    captured_output = mock_stdout.getvalue().strip()
    assert "History saved to history.csv" in captured_output

