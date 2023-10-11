#!/usr/bin/python3
"""Do amazing things with Reddit API
"""


def top_ten(subreddit):
    """Returns top 10 hots posts"""
    import requests
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'alx_project'}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json().get('data')
        for post in data.get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
