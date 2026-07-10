class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        frequency = dict()  
        for index in range(0,len_s):
            if s[index] in frequency:
                frequency[s[index]] +=1
            else:
                frequency[s[index]] = 1

        for index in range(0,len_t):
            if t[index] not in frequency:
                return False
            else:
                frequency[t[index]]-=1

        for _, count in frequency.items():
            if count!= 0:
                return False
        
        return True


        