class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_array = []
        for string in strs:
            encoded_array.append("~~")
            encoded_array.append(string)
        return "".join(encoded_array)

    def decode(self, s: str) -> List[str]:
        print(s)
        # if s == "~~":
        #     return []
        decoded_array = s.split("~~")
        return decoded_array[1:]
