class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        curr = 0
        total = 0
        
        for i in range(n):
            curr += gas[i]
            curr -= cost[i]
            
            if curr < 0:
                start = i + 1
                curr = 0
            
            total += gas[i] - cost[i]
        
        return start if total >= 0 else -1