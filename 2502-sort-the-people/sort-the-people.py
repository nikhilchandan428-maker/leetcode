class Solution:
    def sortPeople(self, names, heights):
        # Pair names and heights together
        people = list(zip(names, heights))
        
        # Sort by height descending
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract names
        return [name for name, height in people]

# Example usage (for testing locally)
sol = Solution()
print(sol.sortPeople(["Mary","John","Emma"], [180,165,170]))  # ['Mary','Emma','John']
print(sol.sortPeople(["Alice","Bob","Bob"], [155,185,150]))    # ['Bob','Alice','Bob']
