# tests the auto feature of whecho using an environment variable $TEST_URL (please set yourself)

import os
import subprocess
import re
import socket
import platform
from whecho import _config as config
import toml

def test_auto_machine():
    # get the test URL
    url = os.environ.get('TEST_URL', None)
    if not url:
        raise ValueError('No test URL passed. Did you set the $TEST_URL environment variable?')
    # use the command line to run whecho and store any errors
    # run initalization command
    command = f"whecho --init"
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    process.stdin.flush()
    # run machine option for name change
    input_text = "machine"
    process.stdin.write(input_text + "\n")
    process.stdin.flush()
    # change machine name to 'auto'
    input_text = "auto"
    process.stdin.write(input_text + "\n")
    process.stdin.flush()
    # exit config
    input_text = "q"
    process.stdin.write(input_text + "\n")
    process.stdin.flush()
    # print stdout and terminate shell after completing change
    stdout, stderr = process.communicate()
    
    process.terminate()

    # check if machine name has been changed to auto
    with open(config.CONFIG_PATH, 'r') as f:
        config_dict = toml.load(f)

    assert config_dict['machine']=="auto"

    send_text = str(config_dict['os']) + ": This is an automated test message."
    print(send_text)
    # use the command line to run whecho and store any errors
    command = f"whecho -u {url} -m {send_text} --debug"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    
    # make sure stderr is a binary empty string
    assert stderr == b''
    
    # extract the Response from stdout (should follow pattern \nResponse: <Response [\d+]>\n)
    response = re.search(r'Response: <Response \[(\d+)\]>', stdout.decode('utf-8'))
    http_code = int(response.group(1))
    # make sure that the HTTP code is in the 200s
    assert http_code >= 200 and http_code < 300

    #extract the machine name from stdout (should follow pattern 'machine': '([^']*)')
    response = re.search(r"'machine': '([^']*)'", stdout.decode('utf-8'))
    machine = str(response.group(1))
    #make sure that the machine name is the same as the hostname
    assert machine == socket.gethostname()
    
if __name__ == "__main__":
    test_auto_machine()
