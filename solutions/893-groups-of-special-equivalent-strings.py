"""
You are given an array A of strings.

A move onto S consists of swapping any two even indexed characters of S, or any two odd indexed characters of S.

Two strings S and T are special-equivalent if after any number of moves onto S, S == T.

For example, S = "zzxy" and T = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz" that swap S[0] and S[2], then S[1] and S[3].

Now, a group of special-equivalent strings from A is a non-empty subset of A such that:

Every pair of strings in the group are special equivalent, and;
The group is the largest size possible (ie., there isn't a string S not in the group such that S is special equivalent to every string in the group)
Return the number of groups of special-equivalent strings from A.


"""

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        group = list()

        count = 0
        for el in A:
            i = 0
            counter = {0: dict(), 1: dict()}
            for ch in el:
                if ch not in counter[i]:
                    counter[i][ch] = 1
                else:
                    counter[i][ch] += 1
                i = 1 - i
            if counter not in group:
                group.append(counter)
                count += 1

        return count