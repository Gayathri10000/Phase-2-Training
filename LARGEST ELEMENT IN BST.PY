class Node:
    def _init_(self,d):
        self.left = None 
        self.right = None 
        self.data = d 
def level_wise_traversal(root):
    queue = [root] 
    res = [] 
    while queue:
        n = len(queue) 
        for i in range(n):
            curr = queue.pop(0) 
            res.append(curr.data) 
            if curr.left:
                queue.append(curr.left) 
            if curr.right:
                queue.append(curr.right) 
    return res  
    
obj1 = Node(10)
obj2 = Node(5)  
obj3 = Node(3)  
obj4 = Node(8)  
obj5 = Node(20)  
obj6 = Node(19) 
obj7 = Node(25)  


obj1.left = obj2 
obj1.right= obj5 
obj2.left = obj3 
obj2.right = obj4 
obj3.left = obj6 
obj3.right = obj7 


r = sorted(level_wise_traversal(obj1)) 
print(r[-1])
