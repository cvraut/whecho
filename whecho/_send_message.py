# sends the message to the specified webhook URL

import requests
from whecho import _config as config

def post_simple(message, url, config=None, debug=False):
    """A simple version of the whecho post. Only includes username & content."""
    if not config:
        config = config.get_config()
        if not url:
            url = config['default_url']
    data = get_data(config,message,url,debug)
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

def get_data(config,message,url,debug=False):
    """General get data function for all supported webhooks."""
    url_keyword_map = {"discord.com": get_discord_data,
                       "slack.com": get_slack_data,
                       "webhook.office.com": get_teams_data,
                       "webexapis.com": get_webex_data}
    for keyword in url_keyword_map:
        if keyword in url:
            if debug:
                print(f"Detected {keyword} in URL")
            return url_keyword_map[keyword](config,message)
    else:
        if debug:
            print(f"Detected unsupported URL: ",end="")
            print(f"{url.split('/')[2]}")
            print("attempting to send to generic webhook with text field in json post body.")
        return get_default_data(config,message)

def get_discord_data(config,message):
    """Get the data to send to discord."""
    data = {'username': f"{config['user']}@{config['machine']}", 
            'content': message}
    return data

def get_slack_data(config,message):
    """Get the data to send to slack."""
    data = {'text': message}
    return data

def get_teams_data(config,message):
    """Get the data to send to teams."""
    data = {'text': message}
    return data

def get_webex_data(config,message):
    """Get the data to send to webex."""
    data = {'markdown': message}
    return data

def get_default_data(config,message):
    """Get the data to send to a generic webhook."""
    data = {'text': message}
    return data
