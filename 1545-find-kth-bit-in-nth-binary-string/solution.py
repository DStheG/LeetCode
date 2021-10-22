class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            ret = ""
            for c in s:
                ret += "1" if c == "0" else "0"
            return ret

        def getString(n):
            if(n == 1):
                return "0"
            s = getString(n-1)
            return s + "1" + invert(s)[::-1]
        
        return getString(n)[k-1]
        
s = Solution()
print(s.findKthBit(20, 1))