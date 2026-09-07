class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        fc = s[0]
        count_char = {}
        replacements = 0
        ls = 0
        l = 0
        # replacements = current_window_length - count_char[fc]  <= k
        #ls = max(current_window_length, ls)
        # l, r = 0, 0
        for r in range(len(s)):
        # while l <= r:
            # if r > len(s) - 1:
            #     break
            # count[s[r]] += count.get(s[r], 1)
            if s[r] not in count_char:
                count_char[s[r]] = 1
            else:
                count_char[s[r]] += 1
            
            if count_char[fc] < count_char[s[r]]:
                fc = s[r]
            # print("r", r)
            # print("l", l)
            window_length = r - l + 1
            replacements = window_length - count_char[fc]
            # print("replacements", replacements)
            # print("window_length", window_length)
            # print("count_char", count_char)
            if replacements > k:
                count_char[s[l]] -= 1
                l += 1
                # print("removed ", count_char[s[l]])
                continue
            ls = max(window_length, ls)
            # r += 1
            # print("ls", ls)
            # print("===============")

        
        return ls
            

        