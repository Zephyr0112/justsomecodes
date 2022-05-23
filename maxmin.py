class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        x = A 
        x.sort()
        z = x[0]+x[-1]
        return z

    
