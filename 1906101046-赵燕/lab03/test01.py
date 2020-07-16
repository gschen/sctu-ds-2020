class Node():
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None
    def adds(self,arr):
        if type(arr)!=list:
            print('类型错误')
            return
        if len(arr)<1:
            print("数组为空")
            return
        
        #初始化队列,[1,2,3,4,5,6,7,8,9]
        queue=[Node(arr.pop(0))]
        self.root=queue[0]
        while len(arr)>0:
            #取出一个节点
            cur=queue.pop(0)
            #判断其子节点是否为空，为空就插入新值
            if cur.left is None:
                cur.left=Node(arr.pop(0))
                queue.append(cur.left)

            if cur.right is None and len(arr)>0:
                cur.right=Node(arr.pop(0))
                queue.append(cur.right)


    def travel_bfs(self):
        if self.root is None:
            print('树为空')
            return 
        #初始化队列，包含根节点
        queue=[self.root]
        #每次取出一个值
        while len(queue)>0:
            cur=queue.pop(0)
            print(cur.val,end=',')
            #如果子节点有值加入队列中
            if cur.left!=None:queue.append(cur.left)
            if cur.right!=None:queue.append(cur.right)
        print('')
    
    def travel_first(self):
        def travel(node):
            if node is None:
                return
            print(node.val,end=',')
            travel(node.left)
            travel(node.right)
        travel(self.root)
        print('')
    #计数和求和
    def count(self):
        global count
        count=0
        global total
        total=0
        def travel(node):
            if node is None:
                
                return
            global count
            count+=1
            global total
            total+=node.val

            travel(node.left)
            travel(node.right)
            
        travel(self.root)
        print(count,total)
