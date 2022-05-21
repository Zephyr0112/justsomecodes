class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n = len(A)
        ckpt = 0
        for i in range(n):
            if A[i]!=B:
                A[i], A[ckpt] = A[ckpt], A[i]
                ckpt += 1
        return ckpt
