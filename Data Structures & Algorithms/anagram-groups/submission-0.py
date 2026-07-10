class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        result = []
        for index in range(0, len(strs)):
            sorted_strs = ''.join(sorted(strs[index]))
            if sorted_strs in anagrams:
                anagrams[sorted_strs].append(strs[index])
            else:
                anagrams[sorted_strs] = [strs[index]]

        for value in anagrams.values():
            result.append(value)
        return result
        