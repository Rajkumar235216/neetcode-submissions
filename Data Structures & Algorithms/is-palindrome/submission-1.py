class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return False
        stripped_s = re.sub(r"[^a-zA-z0-9]", "", s).lower()
        print(stripped_s)
        # if len(stripped_s)%2 != 0:
        #     return False
        
        start = 0
        end = len(stripped_s) - 1
        while start < end:
            if stripped_s[start] == stripped_s[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        
        return True
        