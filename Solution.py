class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        left = 0
        right = x
        mid = (left + right) // 2
        while left <= right:
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            mid = (left + right) // 2

        return mid




