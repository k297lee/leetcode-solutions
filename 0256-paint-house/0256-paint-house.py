class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in reversed(range(len(costs) - 1)):
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
            costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])
        
        return min(costs[0])