# Microsoft Teams Webhook Setup

This guide explains how to obtain a Microsoft Teams Incoming Webhook URL and configure `whecho` to send messages to a Teams channel.

---

## Prerequisites

- A Microsoft 365 account with access to Microsoft Teams
- Access to a Teams channel where you want to receive notifications
- Permission to add connectors to the channel (channel owner or admin)

---

## Step 1 — Open Channel Connectors

1. In Microsoft Teams, navigate to the team and channel where you want to receive notifications.
2. Click the **•••** (More options) menu next to the channel name.
3. Select **Connectors** (or **Manage channel** → **Connectors** in newer Teams versions).

!!! note "New Teams App"
    In the updated Microsoft Teams app, Connectors may be found under **Manage channel** → **Settings** → **Connectors**. If you cannot find Connectors, check with your Teams administrator, as some organizations restrict app installations.

---

## Step 2 — Add an Incoming Webhook

1. In the Connectors dialog, search for **Incoming Webhook** and click **Add** (or **Configure** if already added).
2. Click **Add** again to confirm.
3. Give the webhook a name (e.g., `whecho`) and optionally upload an image.
4. Click **Create**.
5. Copy the generated webhook URL.

!!! tip
    The webhook URL will look like:
    ```
    https://yourorg.webhook.office.com/webhookb2/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx@...
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
Please enter the new value for default_url: https://yourorg.webhook.office.com/webhookb2/XXXX
Successfully modified default_url to https://yourorg.webhook.office.com/webhookb2/XXXX!

Please enter the number/name of the config option you would like to modify (empty or Q to exit): q
Successfully initialized whecho!
```

---

## Step 4 — Send a Test Message

```bash
$ whecho "Hello from whecho! 🎉"
```

You should see the message appear in the Teams channel.

---

## Message Format

When sending to Microsoft Teams, `whecho` posts a JSON body with:

```json
{
  "text": "your message here"
}
```

Teams supports a limited set of HTML and Markdown within the `text` field. For simple text notifications, plain text works perfectly.

---

## Passing the URL Directly (No Init Required)

You can skip `--init` and pass the webhook URL directly:

```bash
$ whecho -u "https://yourorg.webhook.office.com/webhookb2/..." "Deployment done!"
```

Or from Python:

```python
from whecho.whecho import whecho_simple

whecho_simple("Deployment done!", url="https://yourorg.webhook.office.com/webhookb2/...")
```

---

## References

- [Microsoft — Create Incoming Webhooks with Workflows for Microsoft Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)
- [Microsoft — Office 365 Connector cards](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using)
