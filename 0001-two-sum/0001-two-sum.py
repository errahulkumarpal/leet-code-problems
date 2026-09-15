class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        dump = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in dump:
                return [dump[complement],i]
            dump[num] = i
        return []
