class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        nbs= [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                ln=0
                for nb in nbs:
                    r=nb[0]+i
                    c=nb[1]+j
                    if r< row and r>=0 and c>=0 and c<col and abs(board[r][c])==1:
                        ln+=1
                if board[i][j]==1 and  (ln<2 or ln>3):
                    board[i][j]= -1
                
                if board[i][j] == 0 and ln == 3:
                    board[i][j] = 2
        for i in range(row):
            for j in range(col):
                if board[i][j]>0:
                    board[i][j]=1
                else:
                    board[i][j]=0
                
