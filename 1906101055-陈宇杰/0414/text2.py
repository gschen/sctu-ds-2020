class Node():
    def_init_(self,val=None):
    self . val =va 1
    self . left=None
    self . right=None 


class tree():
    def_init__ (self):
       self . root=None
    def add_ left(self,val):
       node=Node(val)
       if self . root==None:
          self . root=node
        else :
            node.left=self.root.left
            self.root.left=node
    def add_ right(self , val):
        node=Node(va1)
    if self . root==None :
       self . root=node
    else:
       node. r ight=self . root. right
       self . root . right=node

    def travel(self):
        def tra(node):
            if node==None:
                return
            print(node,val)
            tra(node.left)
            tra(node.right)
        tra(self.root)



tree=Tree()
tree. add_ left(10) 
tree . add_ right (20)
tree . add_ 1eft(30)
tree. add_ right (40)
tree . add 1eft(50)

