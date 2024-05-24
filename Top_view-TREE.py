def topViewHelper(root, store, hd, level):

# hd is  horizontal distance 
    '''          
                hd
                (0)
                 0               level 0  
       hd-1     / \    hd+1   
        |      /   \    |
      (-1)   /      \  (1)
            3         5          level 1
          /   \      /  \
         10   8     9    6       level 2

         
    '''




    
    if root == None:
        return 
 
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]
 
    topViewHelper(root.left, store, hd - 1, level + 1)
    topViewHelper(root.right, store, hd + 1, level + 1)
 
def findTopView(root):
    result = []
    if root == None:
        return result
 
    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result
