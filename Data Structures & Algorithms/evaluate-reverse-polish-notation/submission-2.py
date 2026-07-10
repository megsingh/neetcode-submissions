class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ('+', '-', '*', '/')
        for i in range(len(tokens)):
            if tokens[i] in op:
                operand1 = st.pop()
                operand2 = st.pop()

                if tokens[i] == '+':
                    res = operand1+ operand2
                if tokens[i] == '-':
                    res = (operand2- operand1)
                if tokens[i] == '*':
                    res = (operand1 * operand2)
                if tokens[i] == '/':
                    res = int(operand2/ operand1)
                st.append(res)
            else:
                st.append(int(tokens[i]))
        return st.pop()
