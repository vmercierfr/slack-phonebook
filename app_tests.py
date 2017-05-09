import os
import phonebook
import unittest
from mock import patch

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = phonebook.app.app.test_client()

    @patch('slacker_cli.Slacker')
    def test_home(self):
        result = self.app.get('/')

        # Expect HTTP code 200
        self.assertEqual(result.status_code, 200)

        # Expect contents
        assert b'<title>Slack phonebook</title>' in result.data
        assert b'Here is the team!' in result.data

if __name__ == '__main__':
    unittest.main()