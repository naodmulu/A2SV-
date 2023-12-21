class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = 0
        length = len(digits)
        for i in range(length):
            val = val*10
            val += digits[i]
        val += 1
        val = str(val)
        return [int(n) for n  in val ]
        