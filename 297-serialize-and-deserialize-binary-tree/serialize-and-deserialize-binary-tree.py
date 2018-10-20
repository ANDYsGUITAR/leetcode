# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Example: 
#
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
#
#
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                vals.append('$')
        vals = []
        helper(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == '$':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        vals = iter(data.split())
        return helper()
#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         result = []
#         self.BFS(root,result)
#         s = ' '.join(result)
#         print(s)
#         return s
#     def BFS(self,root,result):
#         q = [root]
        
#         while(q):
#             node=q.pop(0)
#             if not node:
#                 result.append("#")
#                 continue
            
#             result.append(str(node.val))
           
#             q.append(node.left)
#             q.append(node.right)
            

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         treeData = data.split()
#         if treeData == ["#"]:
#             return None
#         root = TreeNode(int(treeData.pop(0)))
#         queue = [root]
#         while queue:
#             node = queue.pop(0)
#             left = treeData.pop(0)
#             right = treeData.pop(0)
#             if left == '#':
#                 node.left = None
#             else:
#                 leftNode = TreeNode(int(left))
#                 node.left = leftNode
#                 queue.append(leftNode)
#             if right == '#':
#                 node.right = None
#             else:
#                 rightNode = TreeNode(int(right))
#                 node.right = rightNode
#                 queue.append(rightNode)
#         return root
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
