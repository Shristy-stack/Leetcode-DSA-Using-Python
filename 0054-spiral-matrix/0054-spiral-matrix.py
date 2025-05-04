class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output=[]
        top,bottom=0,len(matrix)
        left,right=0,len(matrix[0])
        while left<right and top<bottom:
            #for top left to right column
            for i in range(left, right):
                output.append(matrix[top][i])
            top=top+1
            #for right top to bottom row
            for i in range(top,bottom):
                output.append(matrix[i][right-1])
            right=right-1
            if not (left<right and top<bottom):
                break
            #for bottom right to left
            for i in range(right-1,left-1,-1):
                output.append(matrix[bottom-1][i])
            bottom=bottom-1
            #for left bottom to top
            for i in range(bottom-1,top-1,-1):
                output.append(matrix[i][left])
            left=left+1
        return output
        