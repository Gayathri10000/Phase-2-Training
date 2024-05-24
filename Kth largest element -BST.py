class Solution:
 
    def collectInorder(self, root, arr):
        if root == None:
            return 
        self.collectInorder(root.left, arr)
        arr.append(root.data)
        self.collectInorder(root.right, arr)
 
    def kthLargest(self,root, k):
        arr = []
        self.collectInorder(root, arr)
        n = len(arr)
        return arr[n - k]
