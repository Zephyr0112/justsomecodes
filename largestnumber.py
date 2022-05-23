class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        x = A
        return("".join(sorted(list(map(str,x)),key=lambda a: a*10)[::-1]) if sum(x)!=0 else "0")
