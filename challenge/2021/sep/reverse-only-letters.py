class Solution:
    def reverseOnlyLetters1(self, s: str) -> str:
        def isAlphabet(c):
            if ( (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
                return True
            return False
        l = 0
        r = len(s) - 1
        S = list(s)
        while (l < r) :
            while(l < len(s) and not isAlphabet(S[l])):
                l += 1
            while(r > -1 and not isAlphabet(S[r])):
                r -= 1
            if (l < len(s) and r > -1 and l < r):
                temp = S[l]
                S[l] = S[r]
                S[r] = temp
            l += 1
            r -= 1
        return ''.join(S)

    # 52ms
    def reverseOnlyLetters2(self, s: str) -> str:
        def isAlphabet(c):
            if ( (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
                return True
            return False
        S = list(s)
        buf = []
        for c in S:
            if (isAlphabet(c)):
                buf.append(c)
        idx = 0
        buf = buf[::-1]
        print(buf)
        for i, c in enumerate(S):
            if (isAlphabet(c)):
                S[i] = buf[idx]
                idx+=1
        return ''.join(S)
    
    # 20ms
    def reverseOnlyLetters3(self, s: str) -> str:
        def isAlphabet(c):
            if ( (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
                return True
            return False
        S = list(s)
        buf = []
        idx = []
        for i, c in enumerate(S):
            if (isAlphabet(c)):
                buf.append(c)
                idx.append(i)
        buf = buf[::-1]
        for i, c in zip(idx, buf):
            S[i] = c
        return ''.join(S)

    def reverseOnlyLetters(self, s: str) -> str:
        def isAlphabet(c):
            if ( (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
                return True
            return False
        S = list(s)
        buf = []
        idx = []
        for i, c in enumerate(S):
            if (isAlphabet(c)):
                buf.insert(0, c)
                idx.append(i)
        for i, c in zip(idx, buf):
            S[i] = c
        return ''.join(S)


s = Solution()
print(s.reverseOnlyLetters("ab-cd"))