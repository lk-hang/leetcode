"""
Given a string s. You shsould re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""

class Solution:
    def sortString(self, s: str) -> str:

        counter = [0] * 26
        length = 0
        for letter in s:
            counter[ord(letter) - 97] += 1
            length += 1

        seen = [i for i, cnt in enumerate(counter) if cnt > 0]
        sol = ""
        while length > 0:
            for i in seen:
                sol += chr(i + 97)
                counter[i] -= 1
                length -= 1
            seen = [i for i in seen if counter[i] > 0]
            for j in seen[::-1]:
                sol += chr(j + 97)
                counter[j] -= 1
                length -= 1
            seen = [i for i in seen if counter[i] > 0]
        return sol
