class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=0
        j=i+1
        while(j<len(A)):
            if(A[i]==A[j]):
                j+=1
            else:
                i+=1
                A[i]=A[j]
        A=A[:i+1]
        return i+1
