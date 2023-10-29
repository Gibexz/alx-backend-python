#!/usr/bin/env python3
"""
module: test_client.py
"""
import unittest
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    unittest for GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_result, mock_get_json):
        """
        org method unittest
        """
        client = GithubOrgClient(org_name)
        mock_get_json.return_value = Mock(return_value=expected_result)
        result = client.org()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
