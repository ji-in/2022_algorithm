from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = [''.join(sorted(x)) for x in strs]
        dic = defaultdict(list)
        for i, word in enumerate(sorted_list):
            dic[word].append(strs[i])
        return list(dic.values())