class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (j-i) in d:
                    d[j-i].append(matrix[i][j])
                else:
                    d[j-i] = list()
                    d[j-i].append(matrix[i][j])
        print(d)
        for k, v in d.items():
            if len(set(v)) != 1:
                return False
        return True
       
                