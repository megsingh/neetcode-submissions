class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        codes = {'2': ['a','b','c'], '3':['d', 'e', 'f'], '4': ['g','h','i'], '5': ['j', 'k', 'l'], '6': ['m','n','o'], '7': ['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9': ['w','x','y','z']}

        res = []
        def letterCombinationHelper(i, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for c in codes[digits[i]]:
                letterCombinationHelper(i+1, comb + c)

        if len(digits) > 0:
            letterCombinationHelper(0,"")
        return res