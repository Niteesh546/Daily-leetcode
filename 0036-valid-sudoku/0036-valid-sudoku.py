class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def traverse(self,rs,re,cs,ce):
            seen=set()
            for r in range(rs,re):
                for c in range(cs,ce):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
            return True

        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]=='.': continue

                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]=='.': continue

                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        for rste in range(0,9,3):
            rete=rste+3
            for cste in range(0,9,3):
                cete=cste+3
                if not traverse(self,rste,rete,cste,cete):
                    return False
        return True


    
           


        
