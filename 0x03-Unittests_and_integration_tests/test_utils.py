#!/usr/bin/env python3
""" Mudule for testing utils.py"""
from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
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
        """ Tests if utils.access_nested_map exceptions"""
        with self.assertRaises(KeyError) as context_manager:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context_manager.exception), repr(expected_msg))
