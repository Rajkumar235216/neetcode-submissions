class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for string in strs:
            sort = str(sorted(string))
            if sort not in d:
                d[sort] = [string]
            else:
                d[sort].append(string)
        return list(d.values())