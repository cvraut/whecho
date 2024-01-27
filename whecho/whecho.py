import argparse
from whecho import utilities

def main():
    # deal with arguments
    parser = argparse.ArgumentParser(prog='whecho', description='Linux echo with webhooks! ⚓')
    parser.add_argument('--version', action='store_true', help='Prints the version of whecho and exits.')
    parser.add_argument('-m', '--msg', help='The message to echo.')
    parser.add_argument('message', nargs='?', help='The message to echo.')
    parser.add_argument('--init', action='store_true', help='Initializes whecho.')
    parser.add_argument('-u', '--url', help='The webhook URL to send the message to.',default=None)
    parser.add_argument('-d', '--debug', action='store_true', help='Whether to print debugging information.')
    args = parser.parse_args()
    
    # check the config file
    if not utilities.check_init() and not args.init:
        print('whecho is not initialized. Please run whecho --init to initialize whecho.')
        exit(1)
    
    # process the arguments
    utilities.process_args(args)

if __name__ == '__main__':
    main()