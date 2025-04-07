import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from history_manager import add_to_history, show_history, clear_history, save_history  # Don't forget to import save_history

def test_add_to_history():
    add_to_history("add 2 3", 5)
    history = show_history()  
    assert len(history) > 0
    # Access the last row using .iloc[-1]
    assert history.iloc[-1].tolist() == ["add 2 3", 5]

def test_clear_history():
    add_to_history("add 2 3", 5)
    clear_history()
    history = show_history()
    assert len(history) == 0

# New test cases
def test_add_to_history_empty_operation():
    add_to_history("", 5)
    history = show_history()
    assert len(history) > 0
    assert history.iloc[-1].tolist() == ["", 5]

def test_add_to_history_invalid_result():
    add_to_history("add 2 3", None)  # None as result
    history = show_history()
    assert len(history) > 0
    assert pd.isna(history.iloc[-1, 1])

def test_show_history_empty():
    clear_history()  # Ensure the history is empty
    history = show_history()
    assert history.empty  # Check that the DataFrame is empty

def test_clear_history_multiple_entries():
    add_to_history("add 1 1", 2)
    add_to_history("subtract 2 1", 1)
    clear_history()
    history = show_history()
    assert history.empty  # Check that the history is empty after clearing

from unittest.mock import patch

def test_save_history():
    add_to_history("add 2 3", 5)
    # Mock the to_csv method to avoid actually creating a file
    with patch("pandas.DataFrame.to_csv") as mock_to_csv:
        save_history("test_history.csv")
        # Ensure that the to_csv method was called with the correct arguments
        mock_to_csv.assert_called_once_with("test_history.csv", index=False)

def test_clear_history_twice():
    add_to_history("add 2 3", 5)
    clear_history()
    clear_history()  # Calling it twice
    history = show_history()
    assert history.empty  # Check if history is still empty after second clear

