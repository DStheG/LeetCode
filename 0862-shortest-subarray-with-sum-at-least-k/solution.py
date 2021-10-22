class Solution:
    def shortestSubarray0(self, nums: list[int], k: int) -> int:
        N = [i for i in nums]

        for i in range(0, len(nums)):
            for j in range(i, len(N)):
                if (N[j] >= k):
                    return i+1
                if (i != j):
                    N[j] += nums[j - i - 1]
        return -1

    def shortestSubarray1(self, nums: list[int], k: int) -> int:
        N = [(nums[0], 0)]
        print(N)
        for i in range(1, len(nums)):
            idx = i - 1
            n = N[idx][0] + nums[i]
            if (n > nums[i]):
                N.append((n, N[idx][1]))
            else:
                N.append((nums[i], i))
            N.append(n)
        print(N)

    def shortestSubarray2(self, nums: list[int], k: int) -> int:
        N = [nums[0]]
        ms = [nums[0]]
        for i in range(1, len(nums)):
            N.append(N[i-1] + nums[i])
            s = ms[i-1] + nums[i] 
            ms.append(max(s, nums[i]))
        for w_size in range(1, len(nums)+1):
            for i in range(w_size - 1, len(nums)):
                print(i, w_size)
                sum = N[i]
                if i - w_size >= 0:
                    sum = sum - N[i-w_size] 
                if(sum >= k):
                    return w_size
        return -1

    def shortestSubarray3(self, nums: list[int], k: int) -> int:
        N = [nums[0]]
        cand = []
        if (nums[0] >= k):
            return 1
        for i in range(1, len(nums)):
            s = nums[i] + N[i-1] if (N[i-1] > 0) else nums[i]
            N.append(s)
            if (N[i] >= k):
                cand.append(i)
        if (len(cand) == 0):
            return -1
        ret = len(nums)
        for c in cand:
            s = nums[c]
            i = 1
            while(s < k):
                s += nums[c-i]
                i += 1
            ret = min(ret, i)
        return ret

    def shortestSubarray4(self, nums: list[int], k: int) -> int:
        l, r = 0, 1
        s = nums[0]
        ret = 0xdeaddead
        while(r != len(nums) or l != len(nums)):
            print(l, r, s)
            if(s >= k):
                if(l < r) :
                    ret = min(r-l, ret)
                    s = s - nums[l]
                    l += 1
                else:
                    s = s + nums[r]
                    r += 1
            else:
                if (l < r and nums[l] < 0):
                    s = s - nums[l]
                    l += 1
                elif(r != len(nums)):
                    s = s + nums[r]
                    r += 1
                else:
                    s = s - nums[l]
                    l += 1
        if (ret == 0xdeaddead):
            ret = -1
        return ret

    def shortestSubarray5(self, nums: list[int], k: int) -> int:
        N = [nums[0]]
        for i in range(1, len(nums)):
            N.append(N[i-1] + nums[i])
        q = []
        ret = len(nums) + 1
        for i in range(0, len(nums)):
            while(len(q) and N[i] - N[q[0]] >= k):
                ret = min(ret, i - N[q.pop(0)])
            while(len(q) and N[i] <= N[q[-1]]):
                q.pop(-1)
            q.append(i)
        return ret if ret <= len(nums) else -1
            
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        N = [0]
        for i in range(0, len(nums)):
            N.append(N[i] + nums[i])
        q = []
        ret = len(nums) + 1
        for i in range(0, len(nums)+1):
            while (q and N[i] - N[q[0]] >= k):
                ret = min(i - q[0], ret)
                del q[0]
            while (q and N[i] <= N[q[-1]]):
                del q[-1]
            q.append(i)
        return ret if ret <= len(nums) else -1


s = Solution()
print(s.shortestSubarray([-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6], 151))