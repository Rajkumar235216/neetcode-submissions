class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = dict()
        max_length = 0
        len_s = len(s)
        # s = 
        right = 0
        i = 0
        while i <= len_s - 1:
            # print("i -- ", i)
            # print("right -- ", right)
            if right > len(s) - 1:
                break
            if s[right] not in counter:
                counter[s[right]] = 1
                right += 1
            elif counter[s[right]] > 1:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
                if counter[s[right]] == 1:
                    right += 1
                
            else:
                counter[s[right]] += 1
            max_length = max(len(counter), max_length)
            # print("counter -- ", counter)

        return max_length
