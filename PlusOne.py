class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while digits[i] == 9 and i >= 0:
            digits[i] = 0
            i -= 1

        if i == -1:
            digits = [1] + digits
        else:
            digits[i] += 1

        return digits