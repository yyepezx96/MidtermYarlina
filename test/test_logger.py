import os
import pytest
import logging
from unittest import mock
from logger import setup_logger  # Import the setup function from your logger.py

@mock.patch('logging.FileHandler')
@mock.patch('logging.StreamHandler')
def test_logging_output(mock_file_handler, mock_stream_handler):
    # Set up environment variables
    os.environ['LOG_LEVEL'] = 'DEBUG'
    os.environ['LOG_FILE'] = 'test.log'
    
    # Initialize logger configuration using setup_logger() from logger.py
    setup_logger()

    # Mock the actual handlers so no file writes happen
    mock_file_handler.return_value = mock.MagicMock(spec=logging.FileHandler)
    mock_stream_handler.return_value = mock.MagicMock(spec=logging.StreamHandler)
    
    # Mock 'setLevel' for both handlers   
    mock_file_handler.return_value.setLevel = mock.MagicMock()
    mock_stream_handler.return_value.setLevel = mock.MagicMock()

    # Set the logging level for the mocked handlers
    mock_file_handler.return_value.setLevel(logging.DEBUG)
    mock_stream_handler.return_value.setLevel(logging.DEBUG)

    # Mock 'handle' for both handlers
    mock_file_handler.return_value.handle = mock.MagicMock()
    mock_stream_handler.return_value.handle = mock.MagicMock()

    # Set a level for the mock handlers
    mock_file_handler.return_value.level = logging.DEBUG
    mock_stream_handler.return_value.level = logging.DEBUG

    # Create a logger and add mocked handlers
    logger = logging.getLogger('test_logger')
    logger.addHandler(mock_file_handler.return_value)
    logger.addHandler(mock_stream_handler.return_value)

    # Perform some logging
    logger.debug('Test debug message')
    logger.info('Test info message')
    logger.warning('Test warning message')
    logger.error('Test error message')
    logger.critical('Test critical message')

    # Ensure that the handle() method was called on the mock handlers for each level
    mock_file_handler.return_value.handle.assert_any_call(mock.ANY)
    mock_stream_handler.return_value.handle.assert_any_call(mock.ANY)

    # Ensure handlers were called for each log level (5 calls for each handler)
    assert mock_file_handler.return_value.handle.call_count == 5
    assert mock_stream_handler.return_value.handle.call_count == 5

