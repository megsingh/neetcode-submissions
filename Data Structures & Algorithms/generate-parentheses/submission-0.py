class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def paranthesis(pos, subset, open_bracket, closed_bracket):
            if pos == 2*n:
                res.append(subset)
                return
            if pos == 0 or open_bracket == closed_bracket:
                subset += "("
                open_bracket+=1
                paranthesis(pos+1, subset, open_bracket, closed_bracket)

            elif open_bracket == n:
                subset += ")"
                closed_bracket+=1
                paranthesis(pos+1, subset, open_bracket, closed_bracket)
            else:
                subset += "("
                open_bracket+=1
                paranthesis(pos+1, subset, open_bracket, closed_bracket)
                open_bracket-=1


                subset = subset[:-1]
                subset += ")"
                closed_bracket+=1
                paranthesis(pos+1, subset, open_bracket, closed_bracket)

        paranthesis(0, "", 0, 0)
        return res

        