from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        maxDeque = deque()
        minDeque = deque()
        
        left = 0
        maxLength = 0
        
        for right in range(len(nums)):
            
            # Maintain decreasing maxDeque
            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            
            # Maintain increasing minDeque
            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()
            minDeque.append(right)
            
            # Shrink window if condition breaks
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                if maxDeque[0] == left:
                    maxDeque.popleft()
                if minDeque[0] == left:
                    minDeque.popleft()
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
