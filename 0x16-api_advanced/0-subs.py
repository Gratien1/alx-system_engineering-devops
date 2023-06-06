#!/usr/bin/python3
"""Do amazing things with reddit APIs
"""


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    import requests
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'alx_project'}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        return resp.json().get('data').get('subscribers')
    else:
        return 0
