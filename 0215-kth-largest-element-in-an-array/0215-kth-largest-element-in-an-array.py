class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            tmp = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[tmp], nums[i] = nums[i], nums[tmp]
                    tmp += 1
            
            nums[right], nums[tmp] = nums[tmp], nums[right]
            return tmp
        
        def select(left: int, right: int, k_smallest) -> int:
            if left == right:
                return nums[left]
            
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)
            
            if k_smallest == pivot_idx:
                return nums[k_smallest]
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            else:
                return select(pivot_idx + 1, right, k_smallest)
        
        return select(0, len(nums) - 1, len(nums) - k)