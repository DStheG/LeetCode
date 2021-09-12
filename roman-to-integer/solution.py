class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
            "I"  : 1,
            "V"  : 5,
            "X"  : 10,
            "L"  : 50,
            "C"  : 100,
            "D"  : 500,
            "M"  : 1000,
        }
        ret = 0
        skip = False
        for idx, c in enumerate(s):
            if skip:
                skip = False
                continue
            if s[idx:idx+2] in table.keys() :
                ret += table[s[idx:idx+2]]
                skip = True
            else :
                ret += table[c]
        return ret
            

s = Solution()
print(s.romanToInt("MCMXCIV"))