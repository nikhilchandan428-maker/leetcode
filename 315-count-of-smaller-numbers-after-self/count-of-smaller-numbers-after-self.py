class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums) # to save counts
        indexed_nums = [(nums[key_index], key_index) for key_index in range(len(nums))] # change the nums into (number, index) pairs
        desc_nums, counts = self.mergeWithCount(indexed_nums, counts) # the helper function returns the descendingly sorted indexed_nums and the counts
        return counts
	
	
    def mergeWithCount(self, nums, counts):
        if len(nums) == 1:
            return nums, counts

        cur_stack = []
        left, counts = self.mergeWithCount(nums[: len(nums) // 2], counts)
        right, counts = self.mergeWithCount(nums[len(nums) // 2 :], counts)
        
        
        while left and right:
            
            if left[0] > right[0]:
                counts[left[0][1]] += len(right) # left[0] gives a (number, index) pair as we defined at the beginning, and left[0][1] returns the original index of the number.
                cur_stack.append(left.pop(0))
            else:
                cur_stack.append(right.pop(0))
                
        if left:
            cur_stack.extend(left)
        else:
            cur_stack.extend(right)
			
        return cur_stack, counts