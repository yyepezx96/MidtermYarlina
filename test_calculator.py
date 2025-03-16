import pytest
from calculator import add, subtract, multiply, divide
from unittest.mock import patch  # Import patch here

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    with pytest.raises(TypeError):
        add("a", 3)

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    with pytest.raises(TypeError):
        subtract(5, "b")

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    with pytest.raises(TypeError):
        multiply("x", 2)

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    with pytest.raises(TypeError):
        divide(5, "y")
    
    # Testing logging functionality (divide by zero case)
    with patch('calculator.logger.warning') as mock_warn:
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)
        mock_warn.assert_called_with('Attempted division by zero!')

    # Testing logging functionality for a successful division
    with patch('calculator.logger.info') as mock_log:
        divide(6, 3)
        mock_log.assert_any_call('Dividing 6 by 3')
        mock_log.assert_any_call('Result of division: 2.0')  # Expecting a float

def test_invalid_input():
    with pytest.raises(TypeError):
        add("a", 3)
    with pytest.raises(TypeError):
        subtract(5, "b")
    with pytest.raises(TypeError):
        multiply("x", 2)
