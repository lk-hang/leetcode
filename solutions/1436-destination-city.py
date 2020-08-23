"""

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

"""

from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures = set()
        seen = set()
        for path in paths:
            dep, arr = path
            departures.add(dep)

            for city in path:
                if city not in seen:
                    seen.add(city)
                else:
                    seen.remove(city)

        for city in seen:
            if city not in departures:
                return city