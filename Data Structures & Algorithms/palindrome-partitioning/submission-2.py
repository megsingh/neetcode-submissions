class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        partitions = []


        def partitionHelper(start):

            if start >= len(s):
                res.append(partitions.copy())
                return
            
            for end in range(start, len(s)):
                if self.is_palindrome(s[start:end+1]):
                    partitions.append(s[start:end+1])
                    partitionHelper(end+1)
                    partitions.pop()
                
        partitionHelper(0)
        return res
            

    def is_palindrome(self,s):
        left = 0
        right  = len(s)-1

        while left <= right:
            if s[left]!= s[right]:
                return False
            left+=1
            right-=1
        return True
        