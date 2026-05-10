class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for val in strs:
            key = "".join(sorted(val))
            if key in seen:
                seen[key].append(val)
            else:
                seen[key] = [val]
        return list(seen.values())