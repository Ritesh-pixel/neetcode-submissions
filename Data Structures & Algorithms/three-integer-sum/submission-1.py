class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = set([])
        for i in range(0, n):
            j, k = i + 1, n - 1
            while j < k:
                while nums[i] + nums[j] + nums[k] > 0 and j < k:
                    k -= 1
                if nums[i] + nums[j] + nums[k] == 0 and i < j and j < k:
                    ans.add((nums[i], nums[j], nums[k]))
                j += 1
        return [[e[0], e[1], e[2]] for e in ans]

