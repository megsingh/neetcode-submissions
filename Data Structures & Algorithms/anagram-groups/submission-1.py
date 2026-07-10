class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr_len = len(strs)

        anagram_map = defaultdict(list)
        for i in range (arr_len):
            occurence = [0]*26
            for c in strs[i]:
                occurence[ord(c) - ord('a')]+=1
            anagram_map[tuple(occurence)].append(strs[i])

        return list(anagram_map.values())
            