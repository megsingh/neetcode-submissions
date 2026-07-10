class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_freq = [0]*26
        s2_freq = [0]*26
        for i in range(len_s1):
            s1_freq[ord(s1[i])- ord('a')] += 1
            s2_freq[ord(s2[i])- ord('a')] += 1            

        l,r = 0, len_s1-1
        while r < len_s2:
            
            is_match = True
            for i in range(26):
                if s1_freq[i]!= s2_freq[i]:
                    is_match = False
                    break
            if not is_match:
                s2_freq[ord(s2[l])- ord('a')]-=1
                l+=1
                r+=1
                if r < len_s2:
                    s2_freq[ord(s2[r])- ord('a')]+=1
            else:
                return True
        return False
            