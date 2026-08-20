class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1            
        
        d = dict(sorted(res.items(), key=lambda x:x[1], reverse=True))
        return list(d.keys())[:k]