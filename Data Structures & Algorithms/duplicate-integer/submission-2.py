class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h={}
        for i in nums:
            if i in h.keys():
                mark=0
                return True
            else:
                h[i]=1
        
        return False