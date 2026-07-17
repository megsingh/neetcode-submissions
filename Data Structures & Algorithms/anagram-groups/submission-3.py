class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for i in range(len(strs)):
            char_arr = [0]*26
            for c in strs[i]:
                char_arr[ord(c) - ord('a')]+=1
            char_str = str(char_arr)

            if char_str in anagram_dict:
                anagram_dict[char_str].append(strs[i])
            else:
                anagram_dict[char_str] = [strs[i]]

        return [anagram for anagram in anagram_dict.values()]