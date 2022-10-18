class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        combinations = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(len(beginWord)):
                combinations[wordList[i][:j] + "*" + wordList[i][j + 1:]].append(i)
        
        q = deque()
        q.append((beginWord, 1))
        
        seen = set()
        while q:
            word, length = q.popleft();
            
            for i in range(len(beginWord)):
                genericWord = word[:i] + "*" + word[i + 1:]
                for j in combinations[genericWord]:
                    if wordList[j] == endWord:
                        return length + 1
                    if wordList[j] not in seen:
                        seen.add(wordList[j])
                        q.append((wordList[j], length + 1))
                combinations[genericWord] = []
        
        return 0
