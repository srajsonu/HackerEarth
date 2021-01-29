from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def cnt_bits(self, mask):
        cnt = 0
        for i in range(32):
            if (mask >> i) & 1:
                cnt += 1
        return cnt

    def dp(self, node, n, E, mask, dp):
        row = self.cnt_bits(mask)
        if E < 0:
            return float('inf')

        if row == n:
            return 0

        if (node, E, mask) in dp:
            return dp[(node, E, mask)]

        ans = float('inf')
        for nxt_node, d, e in self.graph[node]:
            if (mask >> nxt_node) & 1 or (E - e) < 0:
                continue

            ans = min(ans, d + self.dp(nxt_node, n, E - e, mask | (1 << nxt_node), dp))

        dp[(node, E, mask)] = ans
        return ans

    def solve(self, n, m, E):
        dp = {}
        ans = self.dp(0, n, E, 1, dp)
        return ans if ans != float('inf') else -1


S = Solution()
n, m, E = map(int, input().split())
arr = []
for _ in range(m):
    u, v, d, e = map(int, input().split())
    S.graph[u - 1].append((v - 1, d, e))
    S.graph[v - 1].append((u - 1, d, e))

print(S.solve(n, m, E))
