class Solution:
    def makeGood(self, s: str) -> str:
        #Self done
        stack = []
        for i in s:
            if len(stack)==0:
                stack.append(i)
                continue
            if stack[-1]==i.swapcase():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)