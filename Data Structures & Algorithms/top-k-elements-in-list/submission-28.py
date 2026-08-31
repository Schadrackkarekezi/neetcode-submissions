class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = []
        res = []
        for i in counts:
            if len(arr) < k:
                arr.append(counts[i])
        for i in counts:
            if counts[i] in arr:
                res.append(i)

        return res
        
     
        


        




            

        



