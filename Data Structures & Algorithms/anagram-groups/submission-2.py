class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for i in range(len(strs)):
            sorted_str = str(sorted(strs[i]))
                
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(strs[i])
            else:
                anagram_dict[sorted_str] = [strs[i]]

        return [anagram for anagram in anagram_dict.values()]