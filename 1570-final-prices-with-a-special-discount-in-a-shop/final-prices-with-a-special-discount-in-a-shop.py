from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # store indices
        
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                index = stack.pop()
                prices[index] -= prices[i]
            stack.append(i)
        
        return prices
