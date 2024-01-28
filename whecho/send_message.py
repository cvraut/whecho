# sends the message to the specified webhook URL

import requests

def post_simple(message, url, config, debug):
    """A simple version of the whecho post. Only includes username & content."""
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