class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        combinations = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(len(beginWord)):
                combinations[wordList[i][:j] + "*" + wordList[i][j + 1:]].append(i)
        
        q_begin = deque()
        q_end = deque()
        q_begin.append(beginWord)
        q_end.append(endWord)
        
        seen_1 = {beginWord: 1}
        seen_2 = {endWord: 1}
        
        def bfs(q, seen_begin, seen_end):
            q_size = len(q)
            for _ in range(q_size):
                word = q.popleft()
                for i in range(len(beginWord)):
                    genericWord = word[:i] + "*" + word[i + 1:]
                    for j in combinations[genericWord]:
                        if wordList[j] in seen_end:
                            return seen_begin[word] + seen_end[wordList[j]]
                        if wordList[j] not in seen_begin:
                            seen_begin[wordList[j]] = seen_begin[word] + 1
                            q.append(wordList[j])
            return 0
        
        res = 0
        while q_begin and q_end:
            if len(q_begin) <= len(q_end):
                res = bfs(q_begin, seen_1, seen_2)
            else:
                res = bfs(q_end, seen_2, seen_1)
            if res:
                return res
        
        return 0
