class Solution:
    def collectInorder(self, root, arr):
        if root == None:
            return 
        self.collectInorder(root.left, arr)
        arr.append(root.val)
        self.collectInorder(root.right, arr)
 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.collectInorder(root, arr)
        n = len(arr)
        for index in range(1, n):
            if arr[index] <= arr[index - 1]:
                return False 
        return True
