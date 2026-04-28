# Botasaurus
Repo for FB changing IP

## Method 1 – Proxy-based IP rotation

`method1.py` exposes two helpers:

| Function | Description |
|---|---|
| `get_current_ip(proxies=None, timeout=10)` | Returns the current public IP (optionally via a proxy). |
| `change_ip(proxy_url, timeout=10)` | Routes through `proxy_url` and returns the new public IP. |

### Quick start

```python
from method1 import change_ip

new_ip = change_ip("http://user:pass@proxy.example.com:8080")
print("Now appearing as:", new_ip)
```

`proxy_url` can be any HTTP or HTTPS proxy URL:

```
http://host:port
http://user:password@host:port
```

SOCKS5 proxies are also supported if the `requests[socks]` extra is installed:

```
pip install requests[socks]
```

Then use:

```
socks5://host:port
```

### Requirements

```
pip install requests
```
