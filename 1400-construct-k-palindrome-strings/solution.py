class Solution:
    def canConstruct1(self, s: str, k: int) -> bool:
        cnt = [0] * (ord('z') - ord('a') + 1)
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        odd = list(filter(lambda n : n % 2, cnt))
        even = list(filter(lambda n : (n % 2) == 0 and n > 0, cnt))

        if(len(odd) > k):
            return False
        new_even = list(filter(lambda n : n - 1 > 0, odd))
        n = []
        for i in new_even:
            n.append(i-1)

        even += n 
        remain_k = k - len(odd)
        print(even, remain_k)
        if(len(even) < remain_k):
            if(sum(even) >= remain_k):
                N = sum(even) // 2
                while(N != remain_k):
                    print(N, remain_k)
                    remain_k -= 2
                    N -= 1
                    if (N >= remain_k):
                        return True
                    if(N < 0 or remain_k < 0):
                        return False
            return False
        return True
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        ans = 0
        for c in set(s):
            ans += s.count(c) % 2
        print(ans)
        return ans <= k

s = Solution()
print(s.canConstruct(s = "annabelle", k = 2))
print(s.canConstruct(s = "leetcode", k = 3))
print(s.canConstruct(s = "true", k = 4))
print(s.canConstruct(s = "yzyzyzyzyzyzyzy", k = 2))
print(s.canConstruct(s = "cr", k = 7))
print(s.canConstruct(s = "aaa", k = 2))
print(s.canConstruct(s = "qlkzenwmmnpkopu", k = 15))
print(s.canConstruct(s = "ibzkwaxxaggkiwjbeysz", k = 15))
print(s.canConstruct(s = "jzsgpcdzfghubdezelbiowsetvkeiejvmsdqicalofvpupvvqaoaobmgwikreytwqtwleghkoqhdfwlygucnwdcenlkvyqlogkcuqkeezmnjptbdxmynvbqvevkoyxleoqljxsxvvroerdydxbznraneecvtspyxzrqpc", k = 82))