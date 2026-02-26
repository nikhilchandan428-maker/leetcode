from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Initialize DSU
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

        # Union emails within same account
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)

        # Group emails by root parent
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # Build final result
        result = []
        for emails in groups.values():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))

        return result