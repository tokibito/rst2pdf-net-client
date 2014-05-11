from . import const


class Client(object):
    def __init__(self, host=None, scheme=None):
        self.host = host or const.DEFAULT_HOST
        self.scheme = scheme or const.DEFAULT_SCHEME
