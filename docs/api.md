# Python API Reference

`whecho` exposes a small public Python API that lets you send webhook notifications directly from your scripts without using the command line.

---

## `whecho_simple`

```python
from whecho.whecho import whecho_simple
```

Sends a message to a webhook URL using the simple format.

### Signature

```python
def whecho_simple(msg: str, url: str = "", debug: bool = False) -> Optional[requests.models.Response]
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `msg` | `str` | *(required)* | The message text to send. |
| `url` | `str` | `""` | The webhook URL to post to. If empty or omitted, the URL saved via `whecho --init` is used. |
| `debug` | `bool` | `False` | When `True`, prints request details and returns the `Response` object. |

### Returns

- `None` by default.
- `requests.models.Response` when `debug=True`.

### Raises

- `ValueError` — if no URL is provided and no default URL is configured.
- `ValueError` — if `msg` is empty.

### Examples

**Basic usage (uses saved default URL):**

```python
from whecho.whecho import whecho_simple

whecho_simple("Training complete! ✅")
```

**With a specific URL:**

```python
from whecho.whecho import whecho_simple

whecho_simple("Deployment done!", url="https://discord.com/api/webhooks/...")
```

**Debug mode (returns the HTTP response):**

```python
from whecho.whecho import whecho_simple

response = whecho_simple("Hello!", debug=True)
print(response.status_code)
```

**Notify when a long task finishes:**

```python
from whecho.whecho import whecho_simple
import time

def train_model():
    time.sleep(60)  # simulate long task

train_model()
whecho_simple("Model training complete! 🎉")
```

---

## Platform Auto-Detection

`whecho_simple` automatically detects the target platform from the URL and formats the JSON payload accordingly:

| URL contains | Platform | Payload format |
|---|---|---|
| `discord.com` or `discordapp.com` | Discord | `{"username": "user@machine", "content": "..."}` |
| `slack.com` | Slack | `{"text": "..."}` |
| `webhook.office.com` | Microsoft Teams | `{"text": "..."}` |
| `webexapis.com` | Webex | `{"markdown": "..."}` |
| *(anything else)* | Generic | `{"text": "..."}` |

This means `whecho_simple` works out of the box with all supported platforms — no extra configuration needed beyond the URL.

---

## Configuration

The configuration (including the default webhook URL) is stored in a platform-specific location:

| OS | Config path |
|---|---|
| Linux | `~/.config/.whecho/config.toml` |
| macOS | `~/Library/Application Support/.whecho/config.toml` |
| Windows | `%APPDATA%\.whecho\config.toml` |

Run `whecho --init` to set or update the configuration interactively.

### Config fields

| Field | Description |
|---|---|
| `default_url` | The default webhook URL used when no URL is passed. |
| `user` | Your username (auto-detected, used in Discord messages). |
| `machine` | Your machine hostname (auto-detected, used in Discord messages). |
