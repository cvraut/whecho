# tests the simple version of whecho using an environment variable $TEST_URL (please set yourself)

import os
import subprocess
import re
import platform
from whecho.whecho import whecho_simple

def simple_post(env_var='TEST_URL',cli=True):
    # get the test URL
    send_text = str(platform.system()) + " " + str(platform.release()) + ": This is an automated test message."
    url = os.environ.get(f'{env_var}', None)
    if not url:
        raise ValueError(f'No test URL passed. Did you set the ${env_var} environment variable?')
    if cli:
        # use the command line to run whecho and store any errors
        command = f"whecho -u \"{url}\" -m \"{send_text}\" --debug"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        
        # make sure stderr is a binary empty string
        assert stderr == b''
        
        # extract the Response from stdout (should follow pattern \nResponse: <Response [\d+]>\n)
        response = re.search(r'Response: <Response \[(\d+)\]>', stdout.decode('utf-8'))
        http_code = int(response.group(1))
    else:
        resp = whecho_simple(send_text,url,debug=True)
        # extract the HTTP code from the response
        http_code = resp.status_code
    # make sure that the HTTP code is in the 200s
    assert http_code >= 200 and http_code < 300

def test_simple_slack():
    # test slack url with cli
    simple_post('TEST_SLACK_URL')

def test_simple_webex():
    # test webex url with python function
    simple_post('TEST_WEBEX_URL', False)
    

if __name__ == "__main__":
    simple_post() # only test discord with main function (duplicated in test_auto_machine.py)
    test_simple_slack()
    test_simple_webex()
