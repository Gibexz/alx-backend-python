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
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self):
        """
        Test for _punlic_repos_url
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mock_check:

            GithubOrgClient('google')._public_repos_url
            mock_check.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            expected_url = "https://api.github.com/orgs/google/repos"

            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                expected_url
                )


if __name__ == '__main__':
    unittest.main()
