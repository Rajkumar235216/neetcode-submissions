class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "!!"
        return "~~".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "!!":
            return []
        if s == "":
            return [""]
        decoded_array = s.split("~~")
        return decoded_array
