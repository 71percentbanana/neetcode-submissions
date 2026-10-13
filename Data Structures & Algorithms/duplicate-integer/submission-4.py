class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=[]
        flag=False
        for i in nums:
            if i in seen:
                flag= True
            seen.append(i)
        
        return flag

     