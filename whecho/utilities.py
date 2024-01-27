# utilities.py
# author: Chinmay Raut (20240127)
#
# Contains utility functions for the whecho project.

import toml
import os


def get_version():
    """Returns the version of whecho."""
    with open('pyproject.toml', 'r') as f:
        pyproject = toml.load(f)
    return pyproject['tool']['poetry']['version']

def check_init():
    """Checks if whecho --init has been run. If it has, there should be a .whecho directory in the user's home directory."""
    return os.path.isdir(os.path.expanduser('~/.whecho'))

def get_config():
    """Returns the config file as a dictionary."""
    with open(os.path.expanduser('~/.whecho/config.toml'), 'r') as f:
        config = toml.load(f)
    return config