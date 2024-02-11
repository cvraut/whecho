# whecho
linux echo but with webhooks! ⚓

Don't guess when a job is finished! Have it message you!

## requirements
- python 3.6+

## installation
```
pip install whecho
```

## First Time Setup
- obtain a webhook URL
![discord_webhook_example](https://i.imgur.com/f9XnAew.png)
- Currently supports:
  - [discord](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
  - [slack](https://api.slack.com/messaging/webhooks)
  - [webex](https://apphub.webex.com/applications/incoming-webhooks-cisco-systems-38054-23307-75252) (with markdown)
- Initialize the `default_url`
```
$ whecho --init
Current config:
[1] default_url: None
[2] user: craut
[3] machine: craut-spectre

Please enter the number/name of the config option you would like to modify (empty or Q to exit): 1
Please enter the new value for default_url: <WEBHOOK_URL>
Successfully modified default_url to <WEBHOOK_URL>!
Current config:
[1] default_url: <WEBHOOK_URL>
[2] user: craut
[3] machine: craut-spectre

Please enter the number/name of the config option you would like to modify (empty or Q to exit): q
Successfully initialized whecho!
```

## general usage (from shell/console)
```
$ whecho "hello there"
```
![hello_there_discord](https://github.com/cvraut/whecho/blob/main/imgs/hello_there_discord.png?raw=true)

## advanced usage
```
$ whecho --help
usage: whecho [-h] [--version] [-m MSG] [--init] [-u URL] [-d] [MSG [MSG ...]]

Linux echo with webhooks! ⚓

positional arguments:
  MSG                The message to echo.

optional arguments:
  -h, --help         show this help message and exit
  --version          Prints the version of whecho and exits.
  -m MSG, --msg MSG  The message to echo (same as 1st positional argument).
  --init             Initializes whecho. Also used to change current config.
  -u URL, --url URL  The webhook URL to send the message to.
  -d, --debug        Whether to print debugging information.
```