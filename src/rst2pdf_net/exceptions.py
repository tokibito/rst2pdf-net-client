class BaseException(Exception):
    pass


class RequireAccessToken(BaseException):
    pass


class APIError(Exception):
    pass
