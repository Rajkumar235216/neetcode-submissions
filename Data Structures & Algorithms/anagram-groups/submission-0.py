class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        length = len(strs)
        if length == 0 or length == 1:
            return [strs]
        
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
        return list(anagrams.values())