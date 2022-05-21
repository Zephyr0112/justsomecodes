class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        x = A
        for i in range(len(x)):
            x[i] = x[i] + (x[x[i]]%len(x))*len(x)
        for i in range(len(x)):
            x[i] = x[i]//len(x)
        return x        
