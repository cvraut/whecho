# Contains utility functions for the whecho project.

import pkg_resources
import os
from whecho import _config as config
import toml
from whecho import _send_message as send_message

def get_version():
    """Prints the version of whecho and exits."""
    print(pkg_resources.get_distribution('whecho').version)
    exit(0)

def init():
    """Initializes whecho."""
    # check if whecho is already initialized
    if config.check_init():
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
    if not config.check_init() and not args.url and not args.init:
        print('whecho is not initialized with a default url. Please run whecho --init to initialize whecho.')
        exit(1)
    
    if args.init:
        init()
    c = config.get_config(args.debug)
    if args.debug:
        print(f"Config: {c}")
    
    m = args.msg if args.msg else " ".join(args.message)
    if args.debug:
        print(f"Message: {m}")
    if not m and not args.init:
        print('No message passed. Try whecho --help for more info.')
        exit(1)
    elif m:
        url = args.url if args.url else c['default_url']
        # send the message
        send_message.post_simple(m, url, c, args.debug)