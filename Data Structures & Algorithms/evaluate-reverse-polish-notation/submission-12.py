class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        ops = {'+','-','*','/'}
        for n in tokens:   
            if n in ops:
                ix1 = num.pop()
                ix2 = num.pop()
                if n == "+":
                    num.append(ix1+ix2)
                elif n == "*":
                    num.append(ix1*ix2)
                elif n == "-":
                    num.append(ix2-ix1)
                elif n == "/":
                    num.append(int(ix2/ix1))
            else:
                num.append(int(n))
        return 0 if not num else num.pop()