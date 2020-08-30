"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        newS = ""
        for el in S:
            if newS == '':
                newS += el
            elif newS[-1] == el:
                newS = newS[:-1]
            else:
                newS += el
        return newS


