from collections import deque

class Node(object):
     def __init__(self,value):
         self.value = value
         self.left = self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = root

    def insert(self,root,newele):
        if root.value < newele.value:
            if root.right == None:
                root.right = newele
                #print("{} is to the right of {}".format(newele.value,root.value))
            else:
                self.insert(root.right,newele)
        else:
            if root.left == None:
                root.left = newele
                #print("{} is to the left of {}".format(newele.value, root.value))
            else:
                self.insert(root.left,newele)

    def zigzagtraversal(self,root):
        stack1 = []
        stack2 = []
        traversal =[]
        stack1.append(root)
        traversal.append(root.value)
        temp = root
        iteration = 1
        while temp.left != None or temp.right != None:
            temp = stack1.pop()
            if iteration % 2 == 0:
                stack2.append(temp.left)
                stack2.append(temp.right)

            else:
                stack2.append(temp.right)
                stack2.append(temp.left)

            if len(stack1) == 0:
                iteration += 1
                for i in range(0,len(stack2)):
                    temp = stack2[i]
                    traversal.append(temp.value)
                stack1 = stack2
                stack2 = []


            length = len(stack1) - 1
            temp = stack1[length]
        print(traversal)


e1 = Node(100)
bt = BinaryTree(e1)
bt.insert(e1,Node(50))
bt.insert(e1,Node(150))
bt.insert(e1,Node(25))
bt.insert(e1,Node(75))
bt.insert(e1,Node(125))
bt.insert(e1,Node(175))
bt.insert(e1,Node(12))
bt.insert(e1,Node(37))
bt.insert(e1,Node(67))
bt.insert(e1,Node(83))
bt.insert(e1,Node(110))
bt.insert(e1,Node(131))
bt.insert(e1,Node(167))
bt.insert(e1,Node(180))

bt.zigzagtraversal(e1)
