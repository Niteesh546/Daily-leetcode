class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        ans=[]
        rows=0
        cols=0
        rowe=n-1
        cole=m-1
        c=0
        total = m*n
        while c<total:
            
            for i in range(cols,cole+1):
                ans.append(matrix[rows][i])
                c=c+1
            rows+=1

            if c==total:
                break
            #cole , rows>rowe
            for i in range(rows,rowe+1):
                ans.append(matrix[i][cole])
                c=c+1
            cole-=1

            if c==total:
                break
            
            for i in range(cole,cols-1,-1):
                ans.append(matrix[rowe][i])
                c=c+1
            rowe-=1

            if c==total:
                break
            for i in range(rowe,rows-1,-1):
                ans.append(matrix[i][cols])
                c=c+1
            cols+=1

            if c==total:
                break
        return ans

            





        
        