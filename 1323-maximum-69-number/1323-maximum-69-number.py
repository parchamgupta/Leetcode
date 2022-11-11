class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        lst = list(num)
        for i in range(len(lst)):
            if lst[i] == '6':
                lst[i] = '9'
                break
        ans = "".join(lst)
        return ans
