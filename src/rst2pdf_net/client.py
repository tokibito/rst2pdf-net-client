import json
from urllib import urlencode

from . import const
from . import exceptions
from . import utils


class AccessToken(object):
    def __init__(self, token, expire=None, authenticated=False):
        self.token = token
        self.expire = expire
        self.authenticated = authenticated


class DocumentMetaData(object):
    def __init__(self, id, created_at=None, status=None,
                 error=None, download_url=None, page_size=None,
                 embed_font=False, margin_style=None):
        self.id = id
        self.created_at = created_at
        self.status = status
        self.error = error
        self.download_url = download_url
        self.page_size = page_size
        self.embed_font = embed_font
        self.margin_style = margin_style


class Client(object):
    access_token_class = AccessToken
    document_meta_data_class = DocumentMetaData

    def __init__(self, host=None, scheme=None, access_token=None,
                 api_paths=None):
        self.host = host or const.DEFAULT_HOST
        self.scheme = scheme or const.DEFAULT_SCHEME
        self.access_token = access_token
        self.api_paths = api_paths or const.API_PATHS

    def _get(self, url, params=None, headers=None):
        """HTTP GET request
        """
        _headers = {}
        if headers:
            _headers.update(headers)
        if params:
            _params = {}
            for key, value in params.items():
                _params[utils.force_encode(key)] = utils.force_encode(value)
            url += '?{}'.format(urlencode(_params))
        request = utils.make_request(url, headers=_headers.items())
        return utils.urlopen(request)

    def _post(self, url, data=None, headers=None):
        """HTTP POST request
        """
        _headers = {'Content-type': 'application/json'}
        if headers:
            _headers.update(headers)
        if data:
            payload = json.dumps(data)
        else:
            payload = None
        request = utils.make_request(url, headers=_headers.items())
        return utils.urlopen(request, data=payload)

    def parse_response_json(self, response):
        if response.headers['Content-type'] != 'application/json':
            return
        return json.loads(response.read())

    def build_url(self, path):
        return '{scheme}://{host}{path}'.format(
            scheme=self.scheme, host=self.host, path=path)

    def get_anonymous_access_token(self):
        """Get access token of anonymous user
        """
        url = self.build_url(self.api_paths['get_access_token'])
        response = self._post(url)
        data = self.parse_response_json(response)
        if data is None:
            return None
        return self.access_token_class(
            token=data['token'],
            expire=data['expire'],
            authenticated=data['authenticated'])

    def post_document(self, text, page_size='A4', embed_font=False,
                      margin_style='default'):
        """Post document

        :returns: Document ID
        """
        if not self.access_token:
            raise exceptions.RequireAccessToken(
                'This method require access token.')
        url = self.build_url(self.api_paths['post_document'])
        response = self._post(url, data={
            'access_token': self.access_token.token,
            'text': text,
            'page_size': page_size,
            'embed_font': embed_font,
            'margin_style': margin_style})
        data = self.parse_response_json(response)
        if data is None:
            raise exceptions.APIError(data)
        return data['id']

    def get_document(self, document_id):
        """Get document meta data
        """
        if not self.access_token:
            raise exceptions.RequireAccessToken(
                'This method require access token.')
        url = self.build_url(
            self.api_paths['get_document'].format(id=document_id))
        response = self._get(url, params={
            'access_token': self.access_token.token})
        data = self.parse_response_json(response)
        if data is None:
            raise exceptions.APIError
        return self.document_meta_data_class(
            id=data['id'],
            created_at=data['created_at'],
            status=data['status'],
            error=data['error'],
            download_url=data['download_url'],
            page_size=data['page_size'],
            embed_font=data['embed_font'],
            margin_style=data['margin_style'])

    def download_file(self, document_id):
        """Download PDF file
        """
        url = self.build_url(
            self.api_paths['download_file'].format(id=document_id))
        response = self._get(url)
        return response
