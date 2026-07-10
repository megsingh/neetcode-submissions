class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0,0
        str_len = len(s)
        result = 1 if str_len else 0;
        occurence = defaultdict(int)
        while end < str_len:  
            if s[end] in occurence:
                result = max(result, end-start)
                start = max(occurence[s[end]]+1, start)
            
            occurence[s[end]] = end
            end+=1
        
        result = max(result, end-start)
        return result
