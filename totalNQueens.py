class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.r = 0
        k = [-1] * n
        res=0
        def solveNQueens(j):
            for i in range(n):
                if check(i, j):
                    k[j] = i
                    if j == n - 1:
                        self.r += 1
                        nonlocal res
                        res+=1
                    else:
                        solveNQueens(j + 1,)

        def check(j, z):
            for i in range(0,z):
                if j == k[i] or (abs(j - k[i]) == abs(z - i)):
                    return False
            return True

        solveNQueens(0)
        return res
