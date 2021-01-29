class Solution:
    def dp(self, A, row, mask, dp):
        if row == len(A):
            return 0

        if (row, mask) in dp:
            return dp[(row, mask)]

        dp[(row, mask)] = self.dp(A, row+1, mask, dp)
        pMask = 0

        for col in range(len(self.prime)):
            if A[row] % self.prime[col] == 0:
                pMask |= (1 << col)

        if not (mask & pMask):
            dp[(row, mask)] = max(dp[(row, mask)], 1 + self.dp(A, row+1, mask | pMask, dp))

        return dp[(row, mask)]

    def solve(self, A, n):
        m = 51
        sieve = [0 for _ in range(m)]
        self.prime = []

        for i in range(2, m):
            if not sieve[i]:
                self.prime.append(i)
                for j in range(i*i, m, i):
                    sieve[j] = 1

        dp = {}
        return self.dp(A, 0, 0, dp)


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(S.solve(A, N))
