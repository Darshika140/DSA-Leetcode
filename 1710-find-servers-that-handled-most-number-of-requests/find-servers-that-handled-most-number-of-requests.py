from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        available = SortedList(range(k))
        busy = []

        count = [0] * k

        for i in range(len(arrival)):

            # Release servers that have finished
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                available.add(server)

            # No available server
            if not available:
                continue

            # Preferred server
            preferred = i % k

            # Find next available server
            idx = available.bisect_left(preferred)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Assign request
            count[server] += 1

            # Mark server busy
            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]