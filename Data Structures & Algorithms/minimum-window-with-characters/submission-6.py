from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == "" or s == "":
            return ""
        
        have_counter = Counter()
        need_counter = Counter(t)
        have_count, need_count = 0, len(need_counter)
        l = 0
        min_length = float("infinity")
        result = [] #stores start, end index against min_len substring found

        for r in range(len(s)):
            if s[r] in need_counter:
                have_counter[s[r]] = 1 + have_counter.get(s[r], 0)
                if have_counter[s[r]] == need_counter[s[r]]:
                    have_count += 1
            
            while have_count == need_count:
                # print("while result -- ", result)
                # print("r -- ", r, "l -- ", l, "r-l+1 -- ", r-l+1)
                # print("min_length -- ", min_length)
                if (r-l+1) < min_length:
                    min_length = min(min_length, r-l+1)
                    result = [l, r]
                # increase l
                if s[l] in have_counter:
                    have_counter[s[l]] -= 1

                if have_counter[s[l]] < need_counter[s[l]]:
                    have_count -= 1
                l += 1

        # print("result -- ", result)
        if not result:
            return ""
        l, r = result
        return s[l: r+1]
                
                


                        
                
             
        