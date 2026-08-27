class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        for j in nums:
            count[j] = 1 + count.get(j, 0)
        for num , cnt in count.items():
            arr.append([cnt,num])
        arr.sort(reverse=True)
        return arr[:k]
        




            

        

