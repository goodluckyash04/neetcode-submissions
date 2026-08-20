class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}
        
        for idx, n in enumerate(nums):
            comp = target - n

            if comp in exist:
                return [exist[comp], idx]

            exist[n] = idx

        
