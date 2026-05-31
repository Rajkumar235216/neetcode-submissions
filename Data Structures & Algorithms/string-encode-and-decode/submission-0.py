class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += "~~" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_array = s.split("~~")
        return decoded_array[1:]
