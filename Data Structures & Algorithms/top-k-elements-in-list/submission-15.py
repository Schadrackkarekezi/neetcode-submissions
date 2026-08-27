class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        for j in nums:
            count[j] = 1 + count.get(j, 0)
        for i , num in count.items():
            arr.append(i)
        arr.sort()
        return arr[k:]
        




            

        

