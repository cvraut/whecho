# sets the default configs and settings for whecho

import os
import getpass
import pkg_resources
import toml
import socket
import platform

DEFAULT_CONFIG = {'default_url': None,
                  'version': pkg_resources.get_distribution('whecho').version,
                  'user': getpass.getuser(),
                  'os': platform.system(),
                  'machine': socket.gethostname(),}
NOT_MODIFIABLE = ['version', 'os']

# use different locations for different OSes
CONFIG_PATH = {'Linux': os.path.expanduser('~/.config/.whecho/config.toml'),
               'Windows': os.path.expanduser('~\\AppData\\Roaming\\.whecho\\config.toml'),
               'Darwin': os.path.expanduser('~/Library/Application Support/.whecho/config.toml')}[DEFAULT_CONFIG['os']]

def check_init():
    """Checks if whecho --init has been run. If it has, there should be a config.toml file in the CONFIG_PATH."""
    return os.path.exists(CONFIG_PATH)

def create_new_config():
    """Creates a new config file."""
    CONFIG_DIR = os.path.dirname(CONFIG_PATH)
    # create the config directory
    os.makedirs(CONFIG_DIR, exist_ok=True)
    # let the user modify the config
    modified_config = modify_config(DEFAULT_CONFIG)
    
    # return the config
    return modified_config

def save_config(config):
    """Saves the config to the file."""
    with open(CONFIG_PATH, 'w+') as f:
        toml.dump(config, f)
    return config
        
def modify_config(config):
    """Lets the user modify the config."""
    # first display the current config options to the user
    choice = "C"
    while choice:
        num_mapping = display_config(config)
        
        # ask the user for input
        choice = input('Please enter the number/name of the config option you would like to modify (empty or Q to exit): ').strip().lower()
        if choice == 'q':
            break
        # if the user entered a number, modify the config
        if choice != '':
            try:
                if choice not in num_mapping:
                    choice = int(choice)
                key = num_mapping[choice]
                value = input(f'Please enter the new value for {key}: ')
                config[key] = value
                print(f"Successfully modified {key} to {value}!")
            except ValueError:
                print('Please enter a valid config option or number.')
            except KeyError:
                print('Please enter a valid config option or number.')
    # save the config
    return save_config(config)

def get_config(debug=False):
    """Returns the config file as a dictionary."""
    if debug:
        print(f"Config pulled from : {CONFIG_PATH}")
    if check_init():
        with open(CONFIG_PATH, 'r') as f:
            config = toml.load(f)
        # check if the config is not corrupted
        for key in DEFAULT_CONFIG:
            if key not in config:
                print(f"whecho config is corrupted. {key} not found. Loading missing key from default. Please run whecho --init to fix this.")
                config[key] = DEFAULT_CONFIG[key]
        if config['machine'] == 'auto':
            config['machine'] = socket.gethostname()
    else:
        config = DEFAULT_CONFIG
    return config

def display_config(config):
    """Displays the config to the user."""
    print('Current config:')
    num_mapping = {}
    for i,kv in enumerate(i for i in config.items() if i[0] not in NOT_MODIFIABLE):
        key,value = kv
        print(f'[{i+1}] {key}: {value}')
        num_mapping[i+1] = key
    print()
    return num_mapping