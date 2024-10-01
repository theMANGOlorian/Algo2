def canJump(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        T = [False for i in range(n)]
        T[0] = True
        for i in range(n):
            items = nums[i]
            if T[i]:
                nextIndex = i + nums[i]
                if nextIndex < n:
                    T[nextIndex] = True
        
        return T[n-1]

print(canJump([2,0]))