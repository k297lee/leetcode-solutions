class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-val, c) for c, val in counter.items()]
        heapq.heapify(heap)
        
        prevFreq, prevChar = 0, ""
        res = []
        while heap:
            freq, ch = heapq.heappop(heap)
            
            res += [ch]
            
            if prevFreq < 0:
                heapq.heappush(heap, (prevFreq, prevChar))
            
            freq += 1
            prevFreq, prevChar = freq, ch
        
        return "".join(res) if len(res) == len(s) else ""