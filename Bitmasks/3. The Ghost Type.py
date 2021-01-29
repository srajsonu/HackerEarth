class Solution:
    def dp(self, A, i, mask, dp):
        if i == len(A):
            return 1

        ans = 0
        for j in range(i+1, len(A)):
            if (mask >> j) & 1:
                continue

            if A[i] & A[j] == A[i]:
                ans += self.dp(A, i+1,  mask | (1 << j), dp)

        return ans

    def solve(self, A):
        A = [i for i in range(1,A+1)]
        dp = {}

        n = len(A)
        for i in range(n):
            for j in range(i+1, n):
                if A[i] & A[j] == A[i] and i < j:
                    print(A[i], A[j])

if __name__ == '__main__':
    A = 4
    B = Solution()
    print(B.solve(A))
