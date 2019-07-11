class Solution(object):
    def solveSudoku(self, board):
        index  = isdot(board)
        seen_set = set()
        for j in range(81):
            if same_row(index,j) or same_col(index,j) or same_threebythree(index,j):
                seen.add(board[j])
        num = set(1,2,3,4,5,6,7,8,9)
        for mynum in num:
            if mynum not in seen_set:
                isdot(board[:index]+mynum+myboar[])
    def isdot(board):
        i = board.find('.')
        if i != -1:
            return i
    def same_row(i,j): 
        return(i/9 == j/9)
    def same_col(i,j):
        return (i-j)%9 == 0
    def same_threebythree(i,j):
        return(i/27 == j/27 and (i%(9/3) ==j%(9/3)))

        '''
        There are N relaxing in a field. They are positioned at points with integer coordinates. Each sheep has a square sunshade, so as not to overheat. The sunshade of a sheep standing at position (X, Y) spreads out to a distance of D from (X, Y), covering a square whose middle is at (X, Y) and whose sides are of length 2D. More precisely, it covers a square with vertices in points (X − D, Y − D), (X − D, Y + D), (X + D, Y − D) and (X + D, Y + D). Sheep are in the centres of their sunshades. Sunshades edges are parallel to the coordinate axes
