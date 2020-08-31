"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if any(all(el.lower() in row for el in word) for row in [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")])]
