class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join(c for c in s if c.isalnum())
        v = []
        for spa in strs:
            v.append(spa.lower())
        lid,rid = 0,len(v)-1
        while(lid<=rid):
            left , right = v[lid], v[rid]
            if(left != right):
                return False
            lid+=1;rid-=1
        return True
        


