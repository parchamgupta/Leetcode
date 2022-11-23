class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in d:
                        return False
                    else:
                        d[board[i][j]] = 1
                    #print(board[i][j], end = " ")
            #print()
  
        for i in range(9):
            d = {}
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in d:
                        return False
                    else:
                        d[board[j][i]] = 1
                    #print(board[j][i], end = " ")
            #print()
                    

        for l in range(0, 7, 3):
            for k in range(0, 7, 3):
                d = {}
                for i in range(l, l + 3):
                    for j in range(k, k + 3):
                        if board[i][j] != '.':
                            if board[i][j] in d:
                                return False
                            else:
                                d[board[i][j]] = 1
                            #print(board[i][j], end = " ")
                #print()
                
        return True
            