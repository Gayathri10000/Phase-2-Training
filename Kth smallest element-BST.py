class Solution:
 
    def collectInorder(self, root, arr):
        if root == None:
            return 
        self.collectInorder(root.left, arr)
        arr.append(root.data)
        self.collectInorder(root.right, arr)
 
    def KthSmallestElement(self,root, K):
        arr = []
        self.collectInorder(root, arr)
        n = len(arr)
        if n < K:
            return -1
        return arr[K - 1] 
