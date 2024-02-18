class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_flag = False
        print(count)
        for value in count.values():
            if value%2:
                odd_flag = True
                length += value -1
            else:
                length += value
        if odd_flag:
            length += 1
        return length

        