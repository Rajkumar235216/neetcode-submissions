from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        opd = {"(": ")", "{": "}", "[": "]"}

        for b in s:
            if b in opd:
                d.append(b)
            else:
                if len(d) >0:
                    cb = d.pop()
                    if opd[cb] == b:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(d) > 0:
            return False
        return True
