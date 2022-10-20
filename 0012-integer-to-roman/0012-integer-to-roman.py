class Solution:
    def val(self, n: int, pow: int) -> str:
        temp = n * 10**pow
        res = ''
        if pow == 3:
            res = res + 'M'
            res = res * n
        elif pow == 2:
            if n == 5:
                res = res + 'D'
            elif n <= 3:
                res = res + 'C'
                res = res * n
            elif n == 4:
                res = res + 'CD'
            elif n > 5 and n <= 8:
                res = res + 'D' + ('C'*(n - 5))
            elif n == 9:
                res = res + 'CM'
        elif pow == 1:
            if n == 5:
                res = res + 'L'
            elif n <= 3:
                res = res + 'X'
                res = res * n
            elif n == 4:
                res = res + 'XL'
            elif n > 5 and n <= 8:
                res = res + 'L' + ('X'*(n - 5))
            elif n == 9:
                res = res + 'XC'
            
        elif pow == 0:
            if n == 5:
                res = res + 'V'
            elif n <= 3:
                res = res + 'I'
                res = res * n
            elif n == 4:
                res = res + 'IV'
            elif n > 5 and n <= 8:
                res = res + 'V' + ('I'*(n - 5))
            elif n == 9:
                res = res + 'IX'   
        return res
        
    def intToRoman(self, num: int) -> str:
        n = len(str(num)) - 1
        temp = num
        d = temp // 10**n
        temp = temp % 10**n
        ans = ''
        while n >= 0:
            ans = ans + self.val(d, n)
            n = n - 1
            d = temp // 10**n
            temp = temp % 10**n 
        return ans