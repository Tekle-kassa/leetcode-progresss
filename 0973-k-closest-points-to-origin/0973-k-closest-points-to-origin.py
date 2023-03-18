class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        res=[]
        obj1=defaultdict(bool)
        for i in range(len(points)):
            s=points[i][0]**2+points[i][1]**2
            if not obj1[s]:
                obj1[s]=[points[i]]
            else:
                obj1[s].append(points[i])
            arr.append(s)
        arr.sort()
        
        for i in range(k):
            res.append(obj1[arr[i]].pop())
        return res