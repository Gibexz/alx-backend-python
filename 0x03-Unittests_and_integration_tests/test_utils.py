#!/usr/bin/env python3
"""
module: test_utils.py
"""
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    unitest for the method utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    unitest for the method utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, payload, mockrequests):
        """"""
        mock_response = mockrequests.return_value
        mock_response.json.return_value = payload

        result = get_json(test_url)

        mockrequests.assert_called_once_with(test_url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    unitest for the use of memoization
    """
    class TestClass:
        """ memoization test class"""
        def a_method(self):
            """mmm mmm mmm"""
            return 42

        @memoize
        def a_property(self):
            """mmm mmm mmm"""
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """mmm mmm mmm"""
        testInstance = self.TestClass()

        result1 = testInstance.a_property()
        result2 = testInstance.a_property()

        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
