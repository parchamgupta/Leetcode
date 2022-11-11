class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        l = 0
        r = len(letters) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l <= r:
            if letters[l] in vowels and letters[r] in vowels:
                t = letters[l]
                letters[l] = letters[r]
                letters[r] = t
                l += 1
                r -= 1
            elif letters[l] in vowels:
                r -= 1
            elif letters[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        ans = "".join(letters)
        return ans
