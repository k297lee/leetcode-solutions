class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = arr[-1]
        arr[-1] = -1
        for i in reversed(range(len(arr) - 1)):
            val = arr[i]
            arr[i] = currMax
            currMax = max(currMax, val)
        
        return arr