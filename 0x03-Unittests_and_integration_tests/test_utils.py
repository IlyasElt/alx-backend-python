#!/usr/bin/env python3
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, key):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        self.assertEqual(context.exception.args[0], key)

class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, payload):
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = payload

            result = get_json(url)

            self.assertEqual(result, payload)
            mock_get.assert_called_once_with(url)

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        
        obj = TestClass()

        with patch.object(obj, "a_method", return_value = 42) as mock_method:
            result1 = obj.a_property
            result2 = obj.a_property
            assert result1 == 42
            assert result2 == 42

            mock_method.assert_called_once()

