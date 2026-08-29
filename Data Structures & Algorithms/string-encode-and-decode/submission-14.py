class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '!'
        if len(strs) == 1:
            return ''.join(strs)

        delimiter = "~~"
        return delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            if s == '!':
                return []
            else:
                return [s]
        
        delimiter = "~~"
        return s.split(delimiter)
        

