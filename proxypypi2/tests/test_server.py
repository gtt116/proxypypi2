import unittest

from proxypypi2 import server


class ServerTestCase(unittest.TestCase):
    def test_match_failed_with_two_word(self):
        self.assertFalse(server.match('cliff', 'cliff-tablib-1.1.gz'))

    def test_match_success_not_case_sensitive(self):
        self.assertTrue(server.match('cliff', 'Cliff-1.1.gz'))
        self.assertTrue(server.match('Cliff', 'cliff-1.1.gz'))
