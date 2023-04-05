class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i=0
        j=1
        count=0
        if len(arr)<3:
            return 0
        while arr[i]>=arr[j]:
            i+=1
            j+=1
            if j==len(arr):
                break
        while j+1<len(arr):
            while j<len(arr) and arr[i]>=arr[j]:
                i+=1
                j+=1
            if j==len(arr):
                break
            if j+1<len(arr)and arr[j]<arr[j+1]:
                j+=1
                if j==len(arr):
                    break
                continue
            elif j+1<len(arr)and arr[j]>arr[j+1]:
                while arr[j]>arr[j+1]:
                    j+=1
                    if j+1==len(arr):
                        break
                count=max(count,j-i+1)
                i=j
                j+=1
            else:
                i=j+1
                j+=2
                continue
            count=max(count,j-i+1)
            # print(count)
            # print(arr[i])
            # print(arr[j])
        return count
            