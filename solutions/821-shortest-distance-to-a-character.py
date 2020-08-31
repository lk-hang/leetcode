"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
"""
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        positions = [i for i in range(len(S)) if S[i] == C]
        num_C = len(positions)

        prv, nxt = -1e10, positions[0]
        idx = 1
        sol = []
        for i in range(n):
            if i > nxt:
                prv = nxt
                if num_C > idx:
                    nxt = positions[idx]
                    idx += 1
                else:
                    nxt = 1e10

            sol.append(min(i - prv, nxt - i))
        return sol
