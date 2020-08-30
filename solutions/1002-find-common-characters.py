"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counter = dict()
        for char in A[0]:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for a in A[1:]:
            for key in counter.keys():
                counter[key] = min(a.count(key), counter[key])

        sol = []
        for key in counter.keys():
            for i in range(counter[key]):
                sol.append(key)

        return sol
