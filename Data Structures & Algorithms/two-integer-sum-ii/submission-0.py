class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lid,rid = 0,len(numbers)-1
        while(lid<rid):
            nos = numbers[lid]+numbers[rid]
            if nos == target:
                return [lid+1,rid+1]
            elif nos < target:
                lid+=1;
            else:
                rid-=1;