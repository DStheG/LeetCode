class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4 = IP.split('.')
        ipv6 = IP.split(':')
        def valid_v4(N):
            if(not len(N)):
                return False
            if (len(N) > 1 and N[0] == '0'):
                return False
            for n in N:
                if(n < '0' or n > '9'):
                    return False
            if (int(N) < 256) :
                return True
            else:
                return False
        def valid_v6(N):
            if(not len(N)):
                return False
            if(len(N) > 4):
                return False
            for n in N:
                if(not len(n)):
                    return False
                if(not ((n >= '0' and n <= '9') or (n >= 'a' and n <= 'f'))):
                    return False
            if (int(N, 16) <= int("0xffff", 16)):
                return True
            return False
        if (len(ipv4) == 4) :
            for N in ipv4:
                if (not valid_v4(N)):
                    return "Neither"
            return "IPv4"
        elif (len(ipv6) == 8) :
            for N in ipv6:
                if (not valid_v6(N.lower())):
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"
s = Solution()
print(s.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))
