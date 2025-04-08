import os
import pytest
import logging
from unittest import mock

@mock.patch('logging.FileHandler')
@mock.patch('logging.StreamHandler')
def test_logging_output(mock_file_handler, mock_stream_handler):
    # Set up environment variables
    os.environ['LOG_LEVEL'] = 'DEBUG'
    os.environ['LOG_FILE'] = 'test.log'

    # Mock the actual handlers so no file writes happen
    mock_file_handler.return_value = mock.MagicMock(spec=logging.FileHandler)
    mock_stream_handler.return_value = mock.MagicMock(spec=logging.StreamHandler)

    # Set the logging level for the mocked handlers to be an integer (like logging.DEBUG)
    mock_file_handler.return_value.setLevel(logging.DEBUG)
    mock_stream_handler.return_value.setLevel(logging.DEBUG)

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

    # Verify that the handle() method was called on the mock handlers
    mock_file_handler.return_value.handle.assert_called()
    mock_stream_handler.return_value.handle.assert_called()

    # You can also check how many times the handlers were called
    assert mock_file_handler.return_value.handle.call_count == 5  # For each log level
    assert mock_stream_handler.return_value.handle.call_count == 5  # For each log level
