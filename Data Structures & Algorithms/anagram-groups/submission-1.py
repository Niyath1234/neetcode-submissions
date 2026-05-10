class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            seen[sorteds].append(s)
        return list(seen.values())