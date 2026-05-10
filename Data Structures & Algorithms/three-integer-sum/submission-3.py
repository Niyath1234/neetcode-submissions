class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range (len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lid,rid=i+1,len(nums)-1
            while(lid<rid):
                total = nums[i]+nums[lid]+nums[rid]
                if total == 0:
                    out.append([nums[i],nums[lid],nums[rid]])
                    lid+=1;rid-=1
                    while lid < rid and lid>0 and nums[lid]==nums[lid-1]:
                        lid+=1
                    while lid < rid and rid>0 and nums[rid]==nums[rid+1]:
                        rid-=1
                elif total<0:
                    lid+=1
                else:
                    rid-=1
        return out