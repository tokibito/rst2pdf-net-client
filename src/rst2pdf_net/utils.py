import sys


def urllib_module():
    if sys.hexversion >= 0x020600F0:
        import urllib2
        return urllib2
    else:
        import urllib
        return urllib


def make_request(url, headers=None):
    """Make request object
    """
    urllib = urllib_module()
    request = urllib.Request(url)
    if headers:
        for key, value in headers:
            request.add_header(key, value)
    return request


def urlopen(request, data=None):
    urllib = urllib_module()
    return urllib.urlopen(request, data)
