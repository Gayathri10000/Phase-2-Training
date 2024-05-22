# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q=[root]
        
        while q:
            n=len(q)
            sub=[]
            for i in range(n):
                currnode = q.pop(0)
                sub.append(currnode.val)

                if currnode.left is not None:
                    q.append(currnode.left)

                if currnode.right is not None:
                    q.append(currnode.right)

        return res
