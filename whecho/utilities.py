# utilities.py
# author: Chinmay Raut (20240127)
#
# Contains utility functions for the whecho project.

import pkg_resources
import os


def get_version():
    """Returns the version of whecho."""
    return pkg_resources.get_distribution('whecho').version

def check_init():
    """Checks if whecho --init has been run. If it has, there should be a .whecho directory in the user's home directory."""
    return os.path.isdir(os.path.expanduser('~/.whecho'))

def get_config():
    """Returns the config file as a dictionary."""
    with open(os.path.expanduser('~/.whecho/config.toml'), 'r') as f:
        config = toml.load(f)
    return config