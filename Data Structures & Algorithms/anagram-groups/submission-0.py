class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for word in strs:
            c_arr = [0]*26

            for ch in word:
                i = ord(ch) - ord('a')
                c_arr[i] += 1
            
            key = tuple(c_arr)

            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]

        return list(group.values())
