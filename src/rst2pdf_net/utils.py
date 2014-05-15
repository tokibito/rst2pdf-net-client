import sys


def urllib_module():
    if sys.hexversion >= 0x030000F0:
        import urllib.request
        return urllib.request
    else:
        import urllib2
        return urllib2


def make_request(url, headers=None):
    """Make request object
    """
    urllib = urllib_module()
    request = urllib.Request(url)
    if headers:
        for key, value in headers:
            request.add_header(
                force_encode(key),
                force_encode(value))
    return request


def urlopen(request, data=None):
    urllib = urllib_module()
    return urllib.urlopen(request, data)


def force_encode(text, encoding='utf-8', errors='replace'):
    return text.encode(encoding, errors)
