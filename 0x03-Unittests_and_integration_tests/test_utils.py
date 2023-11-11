#!/usr/bin/env python3
""" Mudule for testing utils.py"""
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import MagicMock, patch
import utils
from utils import access_nested_map, get_json, memoize


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
    def test_get_json(self, test_url, test_payload):
        """ Tests utils.get_json()"""
        with patch('utils.requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """ Tests for the utils.memoize function"""
    @parameterized.expand([
        (23),
        ("Hello", ),
        ([1, 2, 3, 4], )
    ])
    def test_memoize(self, return_value):
        """ Tests the memoize function in utils.py"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=return_value) as mock_method:
            test_object = TestClass()

            result_1 = test_object.a_property
            result_2 = test_object.a_property

            self.assertEqual(result_1, return_value)
            self.assertEqual(result_2, return_value)

            mock_method.assert_called_once()
