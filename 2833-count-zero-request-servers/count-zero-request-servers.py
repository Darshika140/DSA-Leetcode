class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:

        # Sort logs according to timestamp
        logs.sort(key=lambda a: a[1])

        # Store query time and original index
        q = []
        for i in range(len(queries)):
            q.append((queries[i], i))

        # Sort queries by time
        q.sort()

        # Hash map to store server request frequencies
        count = {}

        # Answer array
        ans = [0] * len(queries)

        left = 0
        right = 0

        for time, idx in q:

            # Add requests up to current query time
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove requests outside the time window
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            # Count servers with zero requests
            ans[idx] = n - len(count)

        return ans