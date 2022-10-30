class Solution(object):
    def shortestPath(self, grid, k):
        seen={}
        q=collections.deque([(0,0,k,0)])
        m,n=len(grid),len(grid[0])
        if m==n==1:
            return 0
        while q:
            x,y,k,steps=q.popleft()
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if i==m-1 and j==n-1:
                    return steps+1
                if not (0<=i<m and 0<=j<n) or grid[i][j]==1 and k<=0 or (i,j) in seen and seen[i,j]>=k-(grid[i][j]==1):
                    continue
                seen[i,j]=k-(grid[i][j]==1)
                q.append((i,j,k-(grid[i][j]==1),steps+1))
        return -1
        