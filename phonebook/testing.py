import os
import unittest
from unittest.mock import MagicMock, patch

import app

"""
class SlackClientMock():

    def api_call(self):
        return []

#import sys
#sys.modules['SlackClient'] = SlackClientMock()
"""

class FlaskrTestCase(unittest.TestCase):

    """
    def setUp(self):
        self.app = app.app.test_client()
        pass

    @patch('app.slackclient.SlackClient.api_call')
    def test_home(self, slackclient):

        slackclient.return_value = {'members': ['bbb', 'aa']}

        #MockClass1.api_call() = []

        #mock_slack.api_call.return_value = []

        result = self.app.get('/')

        # Expect HTTP code 200
        self.assertEqual(result.status_code, 200)

        # Expect contents
        assert b'<title>Slack phonebook</title>' in result.data
        assert b'Here is the team!' in result.data
        print(result.data)
    """

    """
    @patch('app.slackclient.SlackClient.api_call')
    def test_app(self, slackclient):

        slackclient.return_value = {'members': [{'deleted': False}]}
        print(app.get_users(''))
    """

    """
    @patch('app.slackclient.SlackClient.api_call')
    def test_app(self, slackclient):

        slackclient.return_value = {'members': [{'deleted': False}]}
        print(app.demo())
    """

    @patch('app.slackclient.SlackClient.api_call')
    def setUp(self, slackclient):
        self.app = app.app.test_client()
        pass

    @patch('app.slackclient.SlackClient.api_call')
    def test_app(self, slackclient):

        slackclient.return_value = {'members': [{'deleted': False}]}
        #print(self.app.app.get_users(''))
        result = self.app.get('/')
        print(result.data)

if __name__ == '__main__':
    unittest.main()