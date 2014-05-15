from unittest import TestCase


class MakeConfigParserTest(TestCase):
    """make_config_parser
    """
    def _getTarget(self):
        from rst2pdf_net import utils
        return utils.make_config_parser

    def _callFUT(self):
        target = self._getTarget()
        return target()

    def test(self):
        result = self._callFUT()
        self.assertEqual(result.__class__.__name__, 'ConfigParser')


class UrllibModuleTest(TestCase):
    """urllib_module
    """
    def _getTarget(self):
        from rst2pdf_net import utils
        return utils.urllib_module

    def _callFUT(self):
        target = self._getTarget()
        return target()

    def test_has_urlopen(self):
        result = self._callFUT()
        self.assertTrue(hasattr(result, 'urlopen'))

    def test_has_request(self):
        result = self._callFUT()
        self.assertTrue(hasattr(result, 'Request'))


class MakeRequestTest(TestCase):
    """make_request
    """
    def _getTarget(self):
        from rst2pdf_net import utils
        return utils.make_request

    def _callFUT(self, url, headers=None):
        target = self._getTarget()
        return target(url, headers)

    def test_headers(self):
        req = self._callFUT('http://example.com/', [('X-spam', 'Egg')])
        self.assertEqual(req.headers[b'X-spam'], b'Egg')


class ForceEncodeTest(TestCase):
    """force_encode
    """
    def _getTarget(self):
        from rst2pdf_net import utils
        return utils.force_encode

    def _callFUT(self, text, encoding='utf-8', errors='replace'):
        target = self._getTarget()
        return target(text, encoding, errors)

    def test_ascii(self):
        self.assertEqual(self._callFUT('Spam'), b'Spam')

    def test_unicode(self):
        self.assertEqual(self._callFUT(u'\u3042'), b'\xe3\x81\x82')
