# Contains utility functions for the whecho project.

import pkg_resources
import os
from whecho import config
import toml
from whecho import send_message

def get_version():
    """Prints the version of whecho and exits."""
    print(pkg_resources.get_distribution('whecho').version)
    exit(0)

def check_init():
    """Checks if whecho --init has been run. If it has, there should be a ~/.whecho/config.toml file in the user's home directory."""
    return os.path.exists(os.path.expanduser('~/.whecho/config.toml'))

def init():
    """Initializes whecho."""
    # check if whecho is already initialized
    if check_init():
        print('whecho is already initialized. Loading config file for changes')
        config.modify_config(config.get_config())
    else:
        # create a new config file
        config.create_new_config()
        print('Successfully initialized whecho!')
    

def process_args(args):
    """Processes the arguments passed to whecho."""
    if args.debug:
        print(f"Arguments passed: {args}")
    if args.version:
        get_version()
        
    # check the config file
    if not check_init() and not args.init:
        print('whecho is not initialized. Please run whecho --init to initialize whecho.')
        exit(1)
    
    if args.init:
        init()
    c = config.get_config()
    if args.debug:
        print(f"Config: {c}")
    
    m = args.msg if args.msg else args.message
    if not m and not args.init:
        print('No message passed. Try whecho --help for more info.')
        exit(1)
    elif m:
        url = args.url if args.url else c['default_url']
        # send the message
        send_message.post_simple(args.message, url, c, args.debug)