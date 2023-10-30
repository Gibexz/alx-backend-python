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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        test for public_repos method
        """
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        }
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        }
                }
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(GithubOrgClient('google').public_repos(),
                             ["episodes.dart", "cpp-netlib",])

            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, licence_key, expected_result: bool):
        """unitest for has_license method"""
        client = GithubOrgClient("google")
        result = client.has_license(repo, licence_key)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
