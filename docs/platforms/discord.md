# Discord Webhook Setup

This guide explains how to obtain a Discord webhook URL and configure `whecho` to send messages to a Discord channel.

---

## Prerequisites

- A Discord account
- Access to a Discord server where you have **Manage Webhooks** permission (or you own the server)

---

## Step 1 — Open Channel Settings

1. Open Discord and navigate to the server and channel where you want to receive notifications.
2. Right-click the channel name and select **Edit Channel**, or click the ⚙️ gear icon next to the channel name.

---

## Step 2 — Create a Webhook

1. In the channel settings sidebar, click **Integrations**.
2. Click **Webhooks**, then click **New Webhook**.
3. Give the webhook a name (e.g., `whecho`) and optionally upload an avatar image.
4. Click **Copy Webhook URL** to copy the URL to your clipboard.
5. Click **Save Changes**.

!!! tip
    The webhook URL will look like:
    ```
    https://discord.com/api/webhooks/1234567890/xxxxxxxxxxxxxxxxxxxx
    ```

---

## Step 3 — Configure whecho

Run the interactive setup and paste your webhook URL:

```bash
$ whecho --init
Current config:
[1] default_url: None
[2] user: myuser
[3] machine: my-machine

Please enter the number/name of the config option you would like to modify (empty or Q to exit): 1
Please enter the new value for default_url: https://discord.com/api/webhooks/1234567890/xxxxxxxxxxxxxxxxxxxx
Successfully modified default_url to https://discord.com/api/webhooks/1234567890/xxxxxxxxxxxxxxxxxxxx!

Please enter the number/name of the config option you would like to modify (empty or Q to exit): q
Successfully initialized whecho!
```

---

## Step 4 — Send a Test Message

```bash
$ whecho "Hello from whecho! 🎉"
```

You should see the message appear in your Discord channel almost immediately.

---

## Message Format

When sending to Discord, `whecho` posts a JSON body with:

```json
{
  "username": "user@machine",
  "content": "your message here"
}
```

The `username` field is set to `<user>@<machine>` using the values from your `whecho` config, so you can tell which machine sent the notification.

---

## Passing the URL Directly (No Init Required)

You can skip `--init` and pass the webhook URL directly:

```bash
$ whecho -u "https://discord.com/api/webhooks/..." "Build complete!"
```

Or from Python:

```python
from whecho.whecho import whecho_simple

whecho_simple("Build complete!", url="https://discord.com/api/webhooks/...")
```

---

## References

- [Discord — Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
- [Discord — Webhook documentation](https://discord.com/developers/docs/resources/webhook)
