import argparse
from whecho import _utilities as utilities
from whecho._send_message import post_simple
import requests
from typing import Optional

def main():
    # deal with arguments
    parser = argparse.ArgumentParser(prog='whecho', description='Linux echo with webhooks! ⚓')
    parser.add_argument('--version', action='store_true', help='Prints the version of whecho and exits.')
    parser.add_argument('-m', '--msg', help='The message to echo (same as 1st positional argument).')
    parser.add_argument('message', metavar="MSG" ,nargs='*', help='The message to echo.')
    parser.add_argument('--init', action='store_true', help='Initializes whecho. Also used to change current config.')
    parser.add_argument('-u', '--url', help='The webhook URL to send the message to.',default=None)
    parser.add_argument('-d', '--debug', action='store_true', help='Whether to print debugging information.')
    args = parser.parse_args()
    
    # process the arguments
    utilities.process_args(args)

def whecho_simple(msg: str,url: str = "",debug: bool = False) -> Optional[requests.models.Response]:
    """
    Makes a post request to the given URL (loads config if not given) using the simple format.

    @param msg: The message to be posted.
    @param url: The webhook URL to send the message to. If not provided or empty, the config will be loaded.
    @param debug: Whether to print debugging information. Defaults to False.
    @return: None. If debug=True, returns the response object from the post request.
    """
    return post_simple(msg,url,debug=debug)
    

if __name__ == '__main__':
    main()