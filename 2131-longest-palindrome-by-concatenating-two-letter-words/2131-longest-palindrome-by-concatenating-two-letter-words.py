class Solution:
    def longestPalindrome(self, words):
        dict1, count1, count2 = Counter(words), 0, 0
    
        for i in dict1:
            if i[0] == i[1]:
                if dict1[i]%2 == 1:
                    count2 = 2
                    count1 += 2*(dict1[i] - 1)
                else:
                    count1 += 2*dict1[i]
            else:
                if i[::-1] in dict1:
                    count1 += 2*min(dict1[i], dict1[i[::-1]])
                
        return count2 + count1