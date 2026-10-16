class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}
        for n in nums:
            if n not in group:
                group[n]=0
            group[n]+=1
        s=sorted(group,key=group.get,reverse=True)
        return s[:k]
