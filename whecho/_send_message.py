# sends the message to the specified webhook URL

import requests
from whecho import _config as config

def post_simple(message, url, config=None, debug=False):
    """A simple version of the whecho post. Only includes username & content."""
    if not config:
        config = config.get_config()
        if not url:
            url = config['default_url']
    if "discord.com" in url:
        if debug:
            print(f"Detected discord.com in URL")
        data = get_discord_data(config, message)
    elif "slack.com" in url:
        if debug:
            print(f"Detected slack.com in URL")
        data = get_slack_data(config, message)
    else:
        if debug:
            print(f"Detected unsupported URL: ",end="")
            print(f"{url.split('/')[2]}")
        data = get_default_data(config, message)
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
        
def get_discord_data(config,message):
    """Get the data to send to discord."""
    data = {'username': f"{config['user']}@{config['machine']}", 
            'content': message}
    return data

def get_slack_data(config,message):
    """Get the data to send to slack."""
    data = {'text': message}
    return data

def get_default_data(config,message):
    """Get the data to send to a generic webhook."""
    data = {'username': f"{config['user']}@{config['machine']}", 
            'content': message}
    return data
