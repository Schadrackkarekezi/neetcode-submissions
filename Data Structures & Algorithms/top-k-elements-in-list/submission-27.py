class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = []
        for i in counts:
            if len(arr) < k:
                arr.append(counts[i])
        return arr
        
     
        


        




            

        



