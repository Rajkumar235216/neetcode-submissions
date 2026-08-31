import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return False
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        left = 0
        right = len(s) - 1
        while left < right:
            # print("left", left)
            # print("right", right)
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True

        