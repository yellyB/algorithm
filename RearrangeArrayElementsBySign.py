class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        positive = 0
        negative = 1
        for num in nums:
            if num > 0:
                res[positive] = num
                positive += 2
            else:
                res[negative] = num
                negative += 2
        return res
