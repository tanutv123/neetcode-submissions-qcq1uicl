class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        new = digits[-1] + 1
        print('new: ', new)
        digits[-1] = new % 10
        carry = new // 10
        print('carry: ', carry)
        n -= 1
        while n >= 0 and carry:
            new = digits[n] + carry
            digits[n] = new % 10
            carry = new // 10
            n -= 1
        if carry:
            digits.insert(0, carry)
        return digits