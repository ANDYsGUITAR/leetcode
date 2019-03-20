# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root
        self.found = False
        self.dfs(curr, word)
        return self.found
        
        
    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.found = True
            return
        if word[0] != '.':
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])
        else:
            for n in node.children.values():
                self.dfs(n, word[1:])
                
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
