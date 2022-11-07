class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        hmap = defaultdict(list)
        for i, c in enumerate(s):
            hmap[c].append(i)
        
        for key in hmap:
            if len(hmap[key]) < 2:
                continue
            
            l, r = hmap[key][0], hmap[key][-1]
            res += len(set(s[l + 1:r]))
        
        return res