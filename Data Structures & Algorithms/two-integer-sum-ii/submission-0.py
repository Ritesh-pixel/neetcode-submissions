class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for left in range(0, n):
            for right in range(left + 1, n):
                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]