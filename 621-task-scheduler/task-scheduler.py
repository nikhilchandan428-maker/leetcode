from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        
        maxFreq = max(freq.values())
        maxCount = list(freq.values()).count(maxFreq)
        
        partCount = maxFreq - 1
        partLength = n + 1
        formula = partCount * partLength + maxCount
        
        return max(len(tasks), formula)
