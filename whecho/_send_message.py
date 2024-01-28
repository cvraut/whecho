# sends the message to the specified webhook URL

import requests
from whecho import _config as config

def post_simple(message, url, config=None, debug=False):
    """A simple version of the whecho post. Only includes username & content."""
    if not config:
        config = config.get_config()
        if not url:
            url = config['default_url']
    
    data = {'username': f"{config['user']}@{config['machine']}", 
            'content': message}
    if debug:
        print(f"Data: {data}")
    if not url:
        raise ValueError('No URL passed. Did you run whecho --init?')
    try:
        r = requests.post(url, json=data)
        if debug:
            print(f"Response: {r}")
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)