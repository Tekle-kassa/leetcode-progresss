class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        row=0
        while i<len(matrix):
            if target<=matrix[i][len(matrix[i])-1]:
                row=i
                break
            else:i+=1
        l,r=0,len(matrix[row])-1
        while l<=r:
            mid=(l+r)//2
            if matrix[row][mid]>target:
                r=mid-1
            elif matrix[row][mid]<target:
                l=mid+1
            else:
                return True
        return False
                