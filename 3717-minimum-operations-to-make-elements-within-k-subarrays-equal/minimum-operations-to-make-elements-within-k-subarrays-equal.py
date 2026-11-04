import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * (n - x + 1)

        lo = []  # max-heap (negatives), median yahin top par
        hi = []  # min-heap
        delayed = defaultdict(int)
        lo_size = hi_size = 0
        lo_sum = hi_sum = 0

        def prune(heap, is_lo):
            while heap:
                v = -heap[0] if is_lo else heap[0]
                if delayed[v] > 0:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            if lo_size > hi_size + 1:
                v = -heapq.heappop(lo)
                lo_size -= 1; lo_sum -= v
                heapq.heappush(hi, v)
                hi_size += 1; hi_sum += v
                prune(lo, True)
            elif lo_size < hi_size:
                v = heapq.heappop(hi)
                hi_size -= 1; hi_sum -= v
                heapq.heappush(lo, -v)
                lo_size += 1; lo_sum += v
                prune(hi, False)

        def add(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v); lo_size += 1; lo_sum += v
            else:
                heapq.heappush(hi, v); hi_size += 1; hi_sum += v
            balance()

        def remove(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            delayed[v] += 1
            if lo and v <= -lo[0]:
                lo_size -= 1; lo_sum -= v
                if v == -lo[0]:
                    prune(lo, True)
            else:
                hi_size -= 1; hi_sum -= v
                if hi and v == hi[0]:
                    prune(hi, False)
            balance()

        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                med = -lo[0]
                cost[i - x + 1] = (med * lo_size - lo_sum) + (hi_sum - med * hi_size)

        INF = float('inf')
        # rolling dp: prev[i] = j-1 windows, cur[i] = j windows (first i elements)
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = cur[i - 1]
                if i >= x and prev[i - x] != INF:
                    c = prev[i - x] + cost[i - x]
                    if c < cur[i]:
                        cur[i] = c
            prev = cur
        return prev[n]