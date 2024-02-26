class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        length = len(s)
        def reversing(s,i):
            if i == length//2:
                return
            s[i],s[length-1-i] = s[length-1-i],s[i]
            reversing(s,i+1)
        reversing(s,0)

