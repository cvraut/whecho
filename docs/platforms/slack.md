# Slack Webhook Setup

This guide explains how to obtain a Slack Incoming Webhook URL and configure `whecho` to send messages to a Slack channel.

---

## Prerequisites

- A Slack account
- A Slack workspace where you have permission to add apps

---

## Step 1 — Create a Slack App

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps) and click **Create New App**.
2. Choose **From scratch**.
3. Enter an App Name (e.g., `whecho`) and select the Slack workspace you want to use.
4. Click **Create App**.

---

## Step 2 — Enable Incoming Webhooks

1. In your app's settings page, click **Incoming Webhooks** in the left sidebar (under **Features**).
2. Toggle the switch to turn **Activate Incoming Webhooks** to **On**.

---

## Step 3 — Add a Webhook to Your Workspace

1. Scroll down and click **Add New Webhook to Workspace**.
2. Select the channel where `whecho` should post messages, then click **Allow**.
3. A new webhook URL will appear under **Webhook URLs for Your Workspace**. Click **Copy** to copy it.

!!! tip
    The webhook URL will look like:
    ```
    https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
    ```

---

## Step 4 — Configure whecho

Run the interactive setup and paste your webhook URL:

```bash
$ whecho --init
Current config:
[1] default_url: None
[2] user: myuser
[3] machine: my-machine

Please enter the number/name of the config option you would like to modify (empty or Q to exit): 1
Please enter the new value for default_url: https://hooks.slack.com/services/T00000000/B00000000/XXXX
Successfully modified default_url to https://hooks.slack.com/services/T00000000/B00000000/XXXX!

Please enter the number/name of the config option you would like to modify (empty or Q to exit): q
Successfully initialized whecho!
```

---

## Step 5 — Send a Test Message

```bash
$ whecho "Hello from whecho! 🎉"
```

You should see the message appear in the selected Slack channel immediately.

---

## Message Format

When sending to Slack, `whecho` posts a JSON body with:

```json
{
  "text": "your message here"
}
```

Slack's Incoming Webhooks support a subset of [mrkdwn formatting](https://api.slack.com/reference/surfaces/formatting), so you can use `*bold*`, `_italic_`, `` `code` ``, and more in your messages.

---

## Passing the URL Directly (No Init Required)

You can skip `--init` and pass the webhook URL directly:

```bash
$ whecho -u "https://hooks.slack.com/services/..." "Deployment done!"
```

Or from Python:

```python
from whecho.whecho import whecho_simple

whecho_simple("Deployment done!", url="https://hooks.slack.com/services/...")
```

---

## References

- [Slack — Sending messages using Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [Slack — Block Kit formatting](https://api.slack.com/block-kit)
