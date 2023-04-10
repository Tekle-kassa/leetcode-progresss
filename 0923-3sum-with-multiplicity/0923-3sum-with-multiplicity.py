class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        res=set()
        counter=Counter(arr)
        for i in range(len(arr)-2):
            j=i+1
            k=len(arr)-1
            while j<k:
                total=arr[i]+arr[j]+arr[k]
                if total==target:
                    res.add((arr[i],arr[j],arr[k]))
                    j+=1
                    k-=1
                elif total<target:
                    j+=1
                else:
                    k-=1
        temp=[]
        for i in res:
            temp.append(list(i))
        tot=0
        for i in temp:
            c=Counter(i)
            pr=1
            j=0
            while j<3:
                inc=c[i[j]]
                pr*=comb(counter[i[j]],c[i[j]])
                j+=inc
            tot+=pr
        return tot%((10**9)+7)
                    