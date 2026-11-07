import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []          # (freeTime, weight, index)
        ans = []
        t = 0

        for j, p in enumerate(tasks):
            t = max(t, j)

            # koi server free nahi -> sabse jaldi free hone wale tak jump
            if not free:
                t = busy[0][0]

            # jo servers time t tak free ho chuke, unhe wapas free heap mein
            while busy and busy[0][0] <= t:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (t + p, w, i))

        return ans