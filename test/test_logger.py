import pytest
import logging
from unittest import mock
import os

@mock.patch('logging.FileHandler')
@mock.patch('logging.StreamHandler')
def test_logging_output(mock_file_handler, mock_stream_handler):
    # Set up environment variables
    os.environ['LOG_LEVEL'] = 'DEBUG'
    os.environ['LOG_FILE'] = 'test.log'

    # Mock the actual handlers so no file writes happen
    mock_file_handler.return_value = mock.MagicMock()
    mock_stream_handler.return_value = mock.MagicMock()

    logger = logging.getLogger('test_logger')

    # Add the mocked handlers to the logger
    logger.addHandler(mock_file_handler.return_value)
    logger.addHandler(mock_stream_handler.return_value)

    # Perform some logging
    logger.debug('Test debug message')
    logger.info('Test info message')
    logger.warning('Test warning message')
    logger.error('Test error message')
    logger.critical('Test critical message')

    # Verify that the log functions were called
    mock_file_handler.return_value.emit.assert_called()
    mock_stream_handler.return_value.emit.assert_called()
