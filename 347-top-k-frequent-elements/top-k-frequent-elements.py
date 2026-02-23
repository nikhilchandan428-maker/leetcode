from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)  # Step 1: Frequency map
        
        # Step 2: Create buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Step 3: Collect top k frequent elements
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result