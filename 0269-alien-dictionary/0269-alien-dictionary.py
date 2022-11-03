class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegrees = Counter({c: 0 for word in words for c in word})
        
        for word1, word2 in zip(words, words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegrees[c2] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""
        res = []
        q = deque()
        for c in indegrees:
            if indegrees[c] == 0:
                q.append(c)
        
        while q:
            c = q.popleft()
            res.append(c)
            for nextChar in graph[c]:
                indegrees[nextChar] -= 1
                if indegrees[nextChar] == 0:
                    q.append(nextChar)
                    
        if len(res) < len(indegrees):
            return ""
    
        return "".join(res)