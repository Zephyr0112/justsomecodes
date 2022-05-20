class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        pascalrow = []
        prev = 1
        pascalrow.append(prev)
        for i in range(1, A + 1):
            curr = (prev * (A - i + 1)) // i
            pascalrow.append(curr)
            prev = curr
        return pascalrow
