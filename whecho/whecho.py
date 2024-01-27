import argparse
from whecho import utilities

def main():
    parser = argparse.ArgumentParser(prog='whecho', description='Linux echo with webhooks! ⚓')
    parser.add_argument('--version', action='version', version=utilities.get_version())
    args = parser.parse_args()
    print(args.version)

if __name__ == '__main__':
    main()