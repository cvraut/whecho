# whecho
linux echo but with webhooks! 🪝

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
![hello_there_discord](imgs/hello_there_discord.png)