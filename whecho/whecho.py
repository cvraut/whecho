import argparse

def main():
    parser = argparse.ArgumentParser(prog='whecho', description='Linux echo with webhooks! ⚓')
    parser.add_argument('--version', action='version', version='0.0.0')
    args = parser.parse_args()
    print(args.version)

if __name__ == '__main__':
    main()