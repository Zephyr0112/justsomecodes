class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        solvent = list(A)
        solver = []
        for i in range(len(A)):
            if A[i]=='(':
                solver.append(A[i])
            else:
                if i==0:
                    return 0
                elif len(solver)==0:
                    return 0
                else:
                    solver.pop()
        if len(solver)==0:
            return 1
        else:
            return 0
