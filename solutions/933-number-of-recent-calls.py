"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.
"""

from collections import deque

class RecentCounter:

    def __init__(self):

        self.count = 0
        self.queue = deque()

    def ping(self, t: int) -> int:
        while (self.count > 0) and (t - self.queue[0] > 3000):
            self.queue.popleft()
            self.count -= 1
        self.queue.append(t)
        self.count += 1
        return self.count