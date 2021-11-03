class Solution:
    def frequencySort(self, s: str) -> str:
        ALPHA = 26
        cnt = [[i, 0] for i in range(ALPHA*2+10)]
        
        def getIdx(c):
            if (c <= '9'):
                return ord(c) - ord('0')
            if (c <= 'Z'):
                return ord(c) - ord('A') + 10
            return ord(c) - ord('a') + 10 + ALPHA
        def getChr(n):
            if (n < 10):
                return chr(ord('0') + n)
            if (n < 36):
                return chr(ord('A') + n - 10)
            return chr(ord('a') + n - 36)
        
        for c in s:
            cnt[getIdx(c)][1] += 1
        cnt.sort(key=lambda x:x[1], reverse=True)

        ret = ""
        for e in cnt:
            if(e[1] == 0):
                break
            ret += getChr(e[0]) * e[1]
        return ret
        
s = Solution()
print(s.frequencySort("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
