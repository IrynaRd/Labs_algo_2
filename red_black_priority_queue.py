class Node:
    def __init__(self, data, priority):
        self.right = None
        self.left = None
        self.data = data
        self.priority = priority
        self.color = 1
        self.parent = None

class RedBlackQueue:
    def __init__(self):
        self.TNULL = Node(None, None)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, data, priority):
        node = Node(data, priority)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        
        y = None
        x = self.root
        
        while x != self.TNULL:
            y = x
            if node.priority > x.priority:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.priority > y.priority:
            y.left = node
        else:
            y.right = node
        
        if node.parent == None:
            node.color = 0
            return
        if node.parent.parent == None:
            return
        self.fix_insert(node)


    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, node):
        while node.parent.color == 1 and node.parent:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if node.color == 1:
                    node.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def max_priority_node(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    
    def delete_fix(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                s = node.parent.right
                if s.color == 1:
                    s.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    s = node.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    node = node.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = node.parent.right
                    s.color = node.parent.color
                    node.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                s = node.parent.left
                if s.color == 1:
                    s.color = 0
                    node.parent.color = 1
                    self.right_rotate(node.parent)
                    s = node.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    node = node.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = node.parent.left
                    s.color = node.parent.color
                    node.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 0

    def pop(self):
        max_priority = self.max_priority_node(self.root)
        if max_priority == self.TNULL:
            return None
        data = max_priority.data
        self.remove(max_priority)
        return data 
    
    def remove(self, node):
        if node.right == self.TNULL or node.left == self.TNULL:
            y = node
        else:
            y = self.max_priority_node(node.right)
        if y.left != self.TNULL:
            x = y.left
        else:
            x = y.right
        x.parent = y.parent
    
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    
        if y != node:
            node.data, node.priority = y.data, y.priority
        if y.color == 0:
            self.delete_fix(x)


    def inorder(self, node):
        if node != self.TNULL:
            self.inorder(node.left)
            print(node.data, end=",")
            self.inorder(node.right)

    def print_queue(self):
        self.inorder(self.root)
        print()

q = RedBlackQueue()
q.insert("A", 1)
q.insert("B", 2)
q.insert("C", 3)
q.insert("D", 4)
q.insert("E", 5)

q.print_queue()
print(q.pop())
q.print_queue()
max_priority = q.max_priority_node(q.root)
q.remove(max_priority)