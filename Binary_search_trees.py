class Tree:
    def __init__(self, initval = None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return

    def isempty(self):
        return(self.value == None)
    def isleaf(self):
        return(self.left.isempty() and self.left.isempty())

    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return

    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.rigth = self.right.right
        return

    # inorder traversal
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder() + [self.value] + self.right.inorder())

    # __str__ function is implicitly invoked by the + operator    
    def __str__(self):
        return(str(self.inorder()))

    # most basic and important operation 
    def find(self,v):
        if self.isempty():
            return(False)
        if self.value == v:
            return(True)
        if v < self.value:
            return(self.left.find(v))
        else:
            return(self.right.find(v))
    def minval(self):
        # assume not empty
        if self.left == None:
            return(self.value)
        else:
            return(self.left.minval())
    def maxval(self):
        #assume not empty
        if self.right == None:
            return(self.value)
        else:
            return(self.rigth.minval())
    
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        elif self.value < v:
            self.right.insert(v)
            return
        elif self.value > v:
            self.left.insert(v)
            return
    def delete(self,v):
        if self.isempty():
            return
        if self.value > v:
            self.left.delete(v)
        if self.value.delete < v:
            self.right.delete(v)
        
        if self.value == v:
            if self.isleaf:
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return

    
    
#driver program

print("enter values to be inserted \n")
t = Tree()
l = [int(i) for i in input().split(" ")]
for i in l:
    t.insert(i)

print(t)






    



