class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = []
        res= []
        for i , c in counts.item():
            arr.append([c, i])
        arr.sort()
        for v in arr:
            arr.append(v)
            if len(res) == K:
                return arr

    
        
     
        


        




            

        



