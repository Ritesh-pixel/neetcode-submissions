class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
    
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1

        sorted_d = sorted(d.items(),key=lambda x:x[1], reverse=True)

        
        res=[item[0] for item in sorted_d[:k]]

        return res
