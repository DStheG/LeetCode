class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hist = [0] * 255
        head = tail = 0

        ret = 0
        
        for head in range(len(s)):
            c = s[head]
            idx = ord(c)
            hist[idx] += 1
            while (hist[idx] > 1):
                hist[ord(s[tail])] -= 1
                tail += 1
            l = (head-tail+1)
            ret = max(l, ret)
        return ret