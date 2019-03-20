# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
#
# 	Only one letter can be changed at a time
# 	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
#
# Note:
#
#
# 	Return an empty list if there is no such transformation sequence.
# 	All words have the same length.
# 	All words contain only lowercase alphabetic characters.
# 	You may assume no duplicates in the word list.
# 	You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#
#
#
#


class Solution:
    def __init__(self):
        self.l = float('inf')
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # wordList = set(wordList)
        # if endWord not in wordList:
        #     return []
        # ans = []
        # def dfs(curr, wordList, path):
        #     if curr == endWord and path + [curr] not in ans and len(path) + 1 <= self.l:
        #         ans.append(path + [curr])
        #         self.l = len(path) + 1
        #     elif sum([1 if curr[i] != endWord[i] else 0 for i in range(len(curr))]) == 1 and path + [curr, endWord] not in ans and len(path) + 2 <= self.l:
        #         ans.append(path + [curr, endWord])
        #         self.l = len(path) + 2
        #     else:
        #         for word in wordList:
        #             diff = [1 if curr[i] != word[i] else 0 for i in range(len(curr))]
        #             if sum(diff) == 1:
        #                 tmp = [x for x in wordList]
        #                 tmp.remove(word)
        #                 dfs(word, tmp, path + [curr])
        # dfs(beginWord, wordList, [])
        # result = []
        # for path in ans:
        #     if len(path) == self.l:
        #         result.append(path)
        # return result
        if not endWord or not beginWord or endWord not in wordList or not wordList:
            return []
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res
