# whecho

**Linux echo with webhooks! ⚓**

Don't guess when a job is finished — have it message you! `whecho` is a command-line tool (and Python library) that sends notifications to messaging platforms like Discord, Slack, Webex, and Microsoft Teams via webhooks, so you know the moment a long-running task completes.

---

## Installation

```bash
pip install whecho
```

**Requirements:** Python 3.6+

---

## Quickstart

### 1. Obtain a Webhook URL

First, generate a webhook URL from your preferred messaging platform:

| Platform | Guide |
|---|---|
| Discord | [Discord Webhook Setup](platforms/discord.md) |
| Slack | [Slack Webhook Setup](platforms/slack.md) |
| Webex | [Webex Webhook Setup](platforms/webex.md) |
| Microsoft Teams | [Teams Webhook Setup](platforms/teams.md) |

### 2. Initialize whecho

Run the interactive setup to save your webhook URL:

```bash
$ whecho --init
Current config:
[1] default_url: None
[2] user: myuser
[3] machine: my-machine

Please enter the number/name of the config option you would like to modify (empty or Q to exit): 1
Please enter the new value for default_url: https://your-webhook-url-here
Successfully modified default_url to https://your-webhook-url-here!
...
Please enter the number/name of the config option you would like to modify (empty or Q to exit): q
Successfully initialized whecho!
```

### 3. Send a Message

```bash
$ whecho "Hello from the terminal!"
```

That's it! Your message will appear in your configured messaging platform immediately.

---

## Usage

### Command-Line

```bash
# Send a message using your saved default webhook
$ whecho "Build complete!"

# Send to a specific webhook URL (no init required)
$ whecho -u https://your-webhook-url "Deployment finished!"

# Use the --msg flag instead of a positional argument
$ whecho --msg "Training complete!"

# Append whecho to any command to be notified when it finishes
$ sleep 60 && whecho "Sleep done!"
```

### Python API

```python
from whecho.whecho import whecho_simple

# Use the saved default URL
whecho_simple("I'm inside Python 🐍")

# Use a specific webhook URL
whecho_simple("Custom URL message", url="https://your-webhook-url")
```

See the [Python API reference](api.md) for full details.

---

## CLI Reference

```
usage: whecho [-h] [--version] [-m MSG] [--init] [-u URL] [-d] [MSG ...]

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

---

## Supported Platforms

whecho automatically detects the target platform from the webhook URL and formats the message accordingly:

- **[Discord](platforms/discord.md)** — sends as a bot message with username set to `user@machine`
- **[Slack](platforms/slack.md)** — sends using Slack's incoming webhook text format
- **[Webex](platforms/webex.md)** — sends with Markdown support
- **[Microsoft Teams](platforms/teams.md)** — sends via Office 365 connector webhooks
- **Generic webhooks** — sends a JSON body with a `text` field

---

## Table of Contents

- [Python API](api.md)
- Messaging Platform Guides
    - [Discord](platforms/discord.md)
    - [Slack](platforms/slack.md)
    - [Webex](platforms/webex.md)
    - [Microsoft Teams](platforms/teams.md)
