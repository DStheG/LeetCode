class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1= [-1] * 255
        map2 = [-1] * 255
        
        for c1, c2 in zip(s, t):
            n1 = ord(c1)
            n2 = ord(c2)
            if (map1[n1] == -1 and map2[n2] == -1):
                map1[n1] = n2
                map2[n2] = n1
            else:
                if(map1[n1] != n2 or map2[n2] != n1):
                    return False
        return True

s = Solution()
print(s.isIsomorphic('egg', 'add'))