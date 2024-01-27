# make sure that the --help option works

import os

def test_help():
    output = os.system("whecho --help")
    assert output == 0, "The --help option did not work."