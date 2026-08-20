class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers, start=1):
            comp = target-n
            if comp in seen:
                return [seen[comp], i]
            seen[n] = i
        return []