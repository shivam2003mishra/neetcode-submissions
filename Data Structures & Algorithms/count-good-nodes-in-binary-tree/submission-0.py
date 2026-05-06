# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxNode):
            count=0
            if not node:
                return 0
            if node.val>=maxNode:
                count=1
            
            maxNode=max(maxNode,node.val)

            count +=dfs(node.left,maxNode)
            count +=dfs(node.right,maxNode)

            return count
        return dfs(root,root.val)