"""
Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.

The function is constantly increasing, i.e.:

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
The function interface is defined like this:

interface CustomFunction {
public:
  // Returns positive integer f(x, y) for any given positive integer x and y.
  int f(int x, int y);
};
For custom testing purposes you're given an integer function_id and a target z as input, where function_id represent one function from an secret internal list, on the examples you'll know only two functions from the list.

You may return the solutions in any order.
"""




"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        sol = []
        y_max = 1000
        for x in range(1, 1001):
            y = 1
            while customfunction.f(x, y)  <= z and y <= y_max:
                if customfunction.f(x, y) == z:
                    sol.append([x, y])
                    y_max = min(y_max, y)
                y += 1

            y_max = min(y_max, y)
            if customfunction.f(x, 1) >= z:
                break
        return sol
