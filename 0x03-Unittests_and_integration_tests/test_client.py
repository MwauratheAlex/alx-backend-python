#!/usr/bin/env python3
""" Module for testing client"""
import client
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(TestCase):
    """ Tests the client.GithubOrgClient class"""
    @parameterized.expand([
        ('google', {1}),
        ('abc', {2}),
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, test_result, mock_get_json):
        """ Tests GithubOrgClient.org"""
        test_client = GithubOrgClient(org_name=test_org_name)
        mock_get_json.return_value = test_result
        self.assertEqual(test_client.org, test_result)
        test_url = test_client.ORG_URL.format(org=test_org_name)
        mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ("Google", {"repos_url": "url_1"},),
        ("abc", {"repos_url": "url_3"},),
        ("x", {"repos_url": 1},),
    ])
    def test_public_repos_url(self, test_org_name, mock_payload):
        """ Tests GithubOrgClient._public_repos_url"""
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mock_payload
            test_client = GithubOrgClient(org_name=test_org_name)
            self.assertEqual(
                test_client._public_repos_url, mock_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """  Unit-tests for  GithubOrgClient.public_repos"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [{"name": "episodes.dart", }, {"name": "kratu", }, ]
        }

        mock_get_json.return_value = test_payload["repos"]
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock
        ) as mock_public_repos_url:

            mock_public_repos_url.return_value = test_payload["repos_url"]

            test_client = GithubOrgClient("test_org")
            test_public_repos = test_client.public_repos()

            expected_public_repos_return = [
                repo["name"] for repo in test_payload["repos"]
            ]

            self.assertEqual(test_public_repos, expected_public_repos_return)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, test_repo, test_license, expected_result):
        """ unit-tests for GithubOrgClient.has_license"""
        self.assertEqual(
                GithubOrgClient.has_license(test_repo, test_license),
                expected_result
        )
