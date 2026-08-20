class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ann_dict = {}
        for s in strs:
            new_s = "".join(sorted(s))
            if new_s in ann_dict:
                ann_dict[new_s].append(s)
            else:
                ann_dict[new_s] = [s]
        
        return list(ann_dict.values())
