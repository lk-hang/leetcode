"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # sol = []
        # for word in s.split(' '):
        #     sol.append(word[::-1])

        return ' '.join([word[::-1] for word in s.split(' ')])

