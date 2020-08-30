"""
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.


"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        num = len(target)

        sol = []
        for i in range(1, n+1):
            sol.append('Push')
            if i != target[0]:
                sol.append('Pop')
            else:
                target.pop(0)
                num -= 1
                if num == 0:
                    return sol
