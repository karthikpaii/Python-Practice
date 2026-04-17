class Solution:
    def canFormPalindrome(self, s):
        freq = {}

        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        
        odd_count = 0
        for val in freq.values():
            if val % 2 != 0:
                odd_count += 1

        
        return odd_count <= 1

s = "baba"
c=Solution()
print(c.canFormPalindrome(s))