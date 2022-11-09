class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heap.append((-a, 'a'))
        if b > 0:
            heap.append((-b, 'b'))
        if c > 0:
            heap.append((-c, 'c'))
        
        heapq.heapify(heap)
        
        res = []
        while heap:
            ch = heapq.heappop(heap)
            
            if len(res) > 1 and res[-1] == res[-2] == ch[1]:
                if heap:
                    ch2 = heapq.heappop(heap)
                    heapq.heappush(heap, ch)
                    ch = ch2
                else:
                    return "".join(res)
                
            rem = -ch[0]
            
            res.append(ch[1])
            rem -= 1
            if rem > 0:
                heapq.heappush(heap, (-rem, ch[1]))
        
        return "".join(res)