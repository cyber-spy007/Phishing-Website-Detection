import re
import urllib.parse


# Basic URL feature extraction


def extract_features(url):
parsed = urllib.parse.urlparse(url)


return [
len(url),
url.count('.'),
1 if 'https' in parsed.scheme else 0,
1 if '@' in url else 0,
1 if '-' in url else 0,
1 if '//' in url else 0,
len(parsed.netloc),
len(parsed.path)
]
