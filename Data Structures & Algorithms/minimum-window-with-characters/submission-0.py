
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        t_freq , s_freq = Counter(t), defaultdict(int)
        
        min_len = float('inf')
        res = [-1, -1]
        l=0
        have, need = 0, len(t_freq)
        for r in range(len(s)):
            s_freq[s[r]]+=1

            if s[r] in t_freq and s_freq[s[r]] == t_freq[s[r]]:
                have+=1

            while have == need:
                len_window = r - l +1
                if len_window < min_len:
                    min_len= len_window
                    res = [l,r]

                s_freq[s[l]]-=1
                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    have-=1

                l+=1

        if min_len == float('inf'): 
            return ""
        else:
            l, r = res
            return s[l:r+1]

                

                