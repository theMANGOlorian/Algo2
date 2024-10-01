
import timeit

""" Due soluzione proposte (la prima è better!)"""

def maxSubArray1(nums):
    n = len(nums)
    a, b = nums[0], 0
    subMax = nums[0]
    
    for i in range(1, n):
        b = max(a + nums[i], nums[i])
        if subMax < b:
            subMax = b
        a = b
    return subMax

def maxSubArray2(nums):
    n = len(nums)
    T = [0 for i in range(n)]
    T[0] = nums[0]
    
    for i in range(1, n):
        T[i] = max(T[i-1] + nums[i], nums[i])
    
    return max(T)

import cProfile

cProfile.run('maxSubArray1(nums)')
cProfile.run('maxSubArray2(nums)')



