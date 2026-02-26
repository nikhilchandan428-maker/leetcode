class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            key = tuple(sorted(word))
            
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
        