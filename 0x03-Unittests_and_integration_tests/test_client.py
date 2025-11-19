#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that org() returns correct value and calls get_json once."""
        # Setup mock return value
        mock_get_json.return_value = {"key": "value"}

        # Create client instance
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Assert the result equals the mock return value
        self.assertEqual(result, {"key": "value"})

        # Assert get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
