class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            differentiator = [0] * 26
            for c in s:
                differentiator[ord(c) - ord('a')] += 1
            res[tuple(differentiator)].append(s)
        return list(res.values())

