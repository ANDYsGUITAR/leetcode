# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#
# 	Only one letter can be changed at a time.
# 	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
#
# Note:
#
#
# 	Return 0 if there is no such transformation sequence.
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
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
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
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#
#
#
#


from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or endWord not in wordList or not wordList:
            return 0
        L = len(beginWord)
        wordList = set(wordList)
        trans_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                trans_dict[word[:i] + '*' + word[i+1:]].append(word)     
        # print(trans_dict)
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current, level = queue.pop(0)
            for i in range(L):
                intermediate = current[:i] + "*" + current[i+1:]
                for word in trans_dict[intermediate]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                trans_dict[intermediate] = []
        return 0
                        
