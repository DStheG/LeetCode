class Solution:
    def removeDuplicates(self, s: str) -> str:
        S = s
        i = 1
        while(i < len(S)):
            if (S[i] == S[i-1]):
                S = S[:i-1] + S[i+1:]
                i = max(1, i - 1)
                continue
            i += 1
        return S