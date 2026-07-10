class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets_st = []
        relations = {')': '(', ']':'[', '}': '{'}

        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                open_brackets_st.append(s[i])
            else:
                if not open_brackets_st: return False
                top_bracket = open_brackets_st.pop()
                if relations[s[i]] != top_bracket:
                    return False
        if open_brackets_st:
            return False
        return True