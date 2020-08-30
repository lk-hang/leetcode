"""
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sol = dict()
        for domain in cpdomains:
            count, url = domain.split(' ')
            levels = url.split('.')
            for i in range(len(levels)):
                sub_url = '.'.join(levels[i:])
                if sub_url not in sol:
                    sol[sub_url] = int(count)
                else:
                    sol[sub_url] += int(count)

        final_sol = []
        for url, count in sol.items():
            final_sol.append(str(count) + ' ' + url)
        return final_sol

