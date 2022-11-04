class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        hmap = defaultdict(int)
        for word in words:
            if word in hmap and hmap[word] > 0:
                hmap[word] -= 1
                res += 4
            else:
                hmap[word[1] + word[0]] += 1
        
        for key, val in hmap.items():
            if val == 1 and key[0] == key[1]:
                res += 2
                break
        
        return res