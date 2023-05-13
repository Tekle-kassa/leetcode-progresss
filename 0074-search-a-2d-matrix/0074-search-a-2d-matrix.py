class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i=0
        tr,br=0,len(matrix)-1
        # row=0
        while tr<=br:
            row=(br+tr)//2
            if target<matrix[row][0]:
                br=row-1
            elif target>matrix[row][-1]:
                tr=row+1
            else:
                break
        if not tr<=br:
            return False
        row=(tr+br)//2
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
                