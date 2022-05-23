class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
        x1 = A[0]
        y1 = B[0]
        dis = 0
        for _ in range (1,len(A)):
            if abs(A[_]-x1)>abs(B[_]-y1):
                dis = dis + abs(A[_]-x1)
                x1 =  A[_]
                y1 = B[_]
            elif abs(A[_]-x1) == abs(B[_]-y1) :
                dis = dis + abs(B[_]-y1)
                x1 = A[_]
                y1 = B[_]
            else:
                dis = dis + abs(B[_]-y1)
                x1 = A[_]
                y1 = B[_]

        return dis
