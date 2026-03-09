# Webex Webhook Setup

This guide explains how to obtain a Webex Incoming Webhook URL and configure `whecho` to send messages to a Webex space.

---

## Prerequisites

- A Webex account (free accounts are supported)
- Access to a Webex space where you want to receive notifications

---

## Step 1 — Open the Webex App Hub

1. Navigate to the [Webex App Hub — Incoming Webhooks](https://apphub.webex.com/applications/incoming-webhooks-cisco-systems-38054-23307-75252) page.
2. Click **Connect** (you may be prompted to sign in with your Webex account).

---

## Step 2 — Create an Incoming Webhook

1. After connecting, fill in the form:
    - **Webhook name** — a label for this webhook (e.g., `whecho`).
    - **Webex Space** — select the space where messages should be posted.
2. Click **Add**.
3. A webhook URL will be generated. Copy it to your clipboard.

!!! tip
    The webhook URL will look like:
    ```
    https://webexapis.com/v1/webhooks/incoming/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
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
Please enter the new value for default_url: https://webexapis.com/v1/webhooks/incoming/XXXX
Successfully modified default_url to https://webexapis.com/v1/webhooks/incoming/XXXX!

Please enter the number/name of the config option you would like to modify (empty or Q to exit): q
Successfully initialized whecho!
```

---

## Step 4 — Send a Test Message

```bash
$ whecho "Hello from whecho! 🎉"
```

You should see the message appear in your Webex space.

---

## Message Format

When sending to Webex, `whecho` posts a JSON body with:

```json
{
  "markdown": "your message here"
}
```

Because the payload uses the `markdown` field, Webex will render Markdown formatting in your messages. This means you can use:

- `**bold**` or `*bold*`
- `_italic_`
- `` `inline code` ``
- ```` ```code blocks``` ````
- `[links](https://example.com)`

### Example with Markdown

```bash
$ whecho "**Training complete!** Accuracy: \`98.5%\`"
```

Or from Python:

```python
from whecho.whecho import whecho_simple

whecho_simple("**Build passed** ✅\nAll 247 tests passed.")
```

---

## Passing the URL Directly (No Init Required)

You can skip `--init` and pass the webhook URL directly:

```bash
$ whecho -u "https://webexapis.com/v1/webhooks/incoming/..." "Task finished!"
```

Or from Python:

```python
from whecho.whecho import whecho_simple

whecho_simple("Task finished!", url="https://webexapis.com/v1/webhooks/incoming/...")
```

---

## References

- [Webex App Hub — Incoming Webhooks](https://apphub.webex.com/applications/incoming-webhooks-cisco-systems-38054-23307-75252)
- [Webex — Formatting messages with Markdown](https://developer.webex.com/docs/basics#formatting-messages)
