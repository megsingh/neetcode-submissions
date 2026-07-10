class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = list()

        def partitionHelper(palindrome_set,curr, pos):
            
            if pos >= len(s):  
                if curr == "":              
                    res.append(palindrome_set[:])
                return

            curr += s[pos]
            if self.is_palindrome(curr):
                palindrome_set.append(curr)
                partitionHelper(palindrome_set, "", pos+1)
                palindrome_set.pop()

            partitionHelper(palindrome_set, curr, pos+1)

        partitionHelper([],"",0)
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
        