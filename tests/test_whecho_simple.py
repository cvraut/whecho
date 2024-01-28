# tests the simple version of whecho using an environment variable $TEST_URL (please set yourself)

import os
import subprocess
import re

def test_simple():
    # get the test URL
    url = os.environ.get('TEST_URL', None)
    if not url:
        raise ValueError('No test URL passed. Did you set the $TEST_URL environment variable?')
    # use the command line to run whecho and store any errors
    command = f"whecho -u {url} -m 'This is an automated test message.' --debug"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    
    print('stdout:', stdout)
    print('stderr:', stderr)
    
    # make sure stderr is a binary empty string
    assert stderr == b''
    
    # extract the Response from stdout (should follow pattern \nResponse: <Response [\d+]>\n)
    response = re.search(r'Response: <Response \[(\d+)\]>', stdout.decode('utf-8'))
    http_code = int(response.group(1))
    # make sure that the HTTP code is in the 200s
    assert http_code >= 200 and http_code < 300
    
if __name__ == "__main__":
    test_simple()