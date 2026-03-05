import os
import subprocess
import re
import platform
from whecho._send_message import post_simple

def test_empty_url():
    # test that an error is raised when no URL is passed
    try:
        post_simple("This should fail", None, conf={"default_url": None})
    except ValueError as e:
        assert str(e) == 'No URL passed. Did you run whecho --init?'
    else:
        assert False, "Expected Error message was not delivered"

def test_no_url_in_config():
    # test that an error is raised when no URL is passed and no URL in config
    try:
        post_simple("This should fail", None, conf={'default_url': None})
    except ValueError as e:
        assert str(e) == 'No URL passed. Did you run whecho --init?'
    else:
        assert False, "Expected Error message was not delivered"

def test_no_message():
    # test that an error is raised when no message is passed
    url = os.environ.get("TEST_URL", None)
    if not url:
        raise ValueError(f'No test URL passed. Did you set the TEST_URL environment variable?')
    try:
        post_simple("", url)
    except ValueError as e:
        assert str(e) == 'No message passed. Try whecho --help for more info.'
    else:
        assert False, "Expected Error message was not delivered"

if __name__ == "__main__":
    test_empty_url()
    test_no_url_in_config()
    test_no_message()