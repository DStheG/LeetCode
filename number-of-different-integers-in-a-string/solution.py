class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = []
        h = {}
        for c in word:
            if c >= '0' and c <= '9':
                s.append(c)
            else:
                if(len(s)) :
                    key = int(''.join(s))
                    h[key] = 1
                    s = []
        if(len(s)) :
            key = int(''.join(s))
            h[key] = 1
        return len(h)

s = Solution()
print(s.numDifferentIntegers("a1b01c001"))