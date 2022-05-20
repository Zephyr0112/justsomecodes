class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        array = A
        number = B
        current = sum(array[0:number])
        largest = current
        for i in range(1,number):
            j = 0-i
            current = (current - array[number-i] + array[j])
            largest = max(current,largest)
        return largest
