class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: remove extra ')'
        result = []
        open_count = 0
        
        for char in s:
            if char == '(':
                open_count += 1
                result.append(char)
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                    result.append(char)
            else:
                result.append(char)
        
        # Second pass: remove extra '('
        final_result = []
        for char in reversed(result):
            if char == '(' and open_count > 0:
                open_count -= 1
            else:
                final_result.append(char)
        
        return ''.join(reversed(final_result))
