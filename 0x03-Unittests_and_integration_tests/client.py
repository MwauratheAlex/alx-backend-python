#!/usr/bin/env python3
"""A github org client
"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """A Githib org client
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Init method of GithubOrgClient"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Memoize org"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Public repos URL"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Memoize repos payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """Public repos"""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Static: has_license"""
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license


def main():
    # Create an instance of GithubOrgClient for a specific organization
    org_name = "google"  # Replace with the name of a GitHub organization
    client = GithubOrgClient(org_name)

    # Fetch organization details
    org_details = client.org  # Access 'org' as an attribute, not a method
    print("Organization Details:")
    print(org_details)

    # Fetch the list of public repositories
    public_repos = client.public_repos()
    print("\nPublic Repositories:")
    for repo in public_repos:
        print(repo)

    # Fetch the list of public repositories with a specific license (optional)
    license_type = "YOUR_LICENSE_TYPE"  # Replace with a license type,e.g."mit"
    public_repos_with_license = client.public_repos(license=license_type)
    print(f"\nPublic Repositories with '{license_type}' License:")
    for repo in public_repos_with_license:
        print(repo)


if __name__ == "__main__":
    main()
