class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = False
        if len(s)!=len(t):
            return False
        for i in s:
            if i in t:
                flag= True
                t=t.replace(i,"",1)
            else:
                flag= False
                return False

        
        
        return flag