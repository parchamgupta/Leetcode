class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = strs.copy()
        
        for i in range(len(lst)):
            lst[i] = ''.join(sorted(lst[i]))
        print(lst)
            
        d = {}
        for i in range(len(strs)):
            if lst[i] in d:
                d[lst[i]].append(i)
            else:
                d[lst[i]] = [i]
        print(d)
        ans = []
        for k, v in d.items():
            row = []
            for i in v:
                row.append(strs[i])
            ans.append(row)
        return ans