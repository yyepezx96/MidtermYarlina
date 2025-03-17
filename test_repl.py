import pytest
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
def test_do_add(mock_calculator):
    # Capture both stdout and stderr
    captured_output = StringIO()
    captured_error = StringIO()

    # Redirect stdout and stderr to the StringIO objects
    calculator_repl = CalculatorREPL()
    calculator_repl.stdout = captured_output
    calculator_repl.stderr = captured_error

    # Run the command (simulate user input for adding)
    calculator_repl.do_add("2 3")

    # Check if the output contains the correct result (stdout)
    assert "5" in captured_output.getvalue()

    # Check if the logger has logged the correct info (stderr)
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
