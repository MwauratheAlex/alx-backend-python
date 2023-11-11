#!/usr/bin/env python3
""" Mudule for testing utils.py"""
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import MagicMock, patch
import utils
from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):
    """ Tests for access_nested_map(nested_map, path)"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests utils.access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        """ Tests utils.access_nested_map exceptions"""
        with self.assertRaises(KeyError) as context_manager:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context_manager.exception), repr(expected_msg))


class TestGetJson(TestCase):
    """ Tests for utils.get_json(url)"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload,  mock_requests):
        """ Tests utils.get_json()"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)
