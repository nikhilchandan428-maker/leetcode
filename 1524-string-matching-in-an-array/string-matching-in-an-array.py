class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    result.append(word)
                    break
        return result