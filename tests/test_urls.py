import unittest
from piglatin import create_app


app = create_app('piglatin.settings.TestConfig')


class TestURLs(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_home(self):
        """ Tests if the home page loads """
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_translate(self):
        """ Tests if the translate page loads """
        result = self.app.get('/translate?text=Something')
        self.assertEqual(result.status_code, 200)

        result = self.app.get('/translate')
        self.assertEqual(result.status_code, 500)
