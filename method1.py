"""
Method 1: IP rotation via proxy server.

This module provides a simple interface for routing requests
through a proxy to present a different IP address.
"""

import requests


def get_current_ip(proxies=None, timeout=10):
    """Return the current public IP address.

    Args:
        proxies (dict, optional): Optional proxy mapping, e.g.
            ``{'http': 'http://host:port', 'https': 'http://host:port'}``.
        timeout (int): Request timeout in seconds.

    Returns:
        str: The current public IP address.
    """
    response = requests.get(
        "https://api.ipify.org?format=json",
        proxies=proxies,
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()["ip"]


def change_ip(proxy_url, timeout=10):
    """Change the apparent IP address by routing through *proxy_url*.

    This is **Method 1** – proxy-based IP rotation.  Pass in any
    HTTP/HTTPS proxy URL and the function returns the new public IP
    address seen from the remote side.

    Args:
        proxy_url (str): Proxy URL in one of these forms:
            - ``"http://host:port"``
            - ``"http://user:password@host:port"``
            - ``"socks5://host:port"`` (requires ``pip install requests[socks]``)
        timeout (int): Request timeout in seconds (default 10).

    Returns:
        str: The public IP address as seen when routing through the proxy.

    Raises:
        ValueError: If *proxy_url* is empty or ``None``.
        requests.HTTPError: If the IP-check endpoint returns an error status.
        requests.RequestException: On connection / timeout errors.

    Example::

        from method1 import change_ip

        new_ip = change_ip("http://user:pass@proxy.example.com:8080")
        print("Now appearing as:", new_ip)
    """
    if not proxy_url:
        raise ValueError("proxy_url must not be empty")

    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    return get_current_ip(proxies=proxies, timeout=timeout)
