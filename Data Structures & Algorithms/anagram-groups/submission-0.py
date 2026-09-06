class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            hm[sorted_str].append(str)
        return list(hm.values())