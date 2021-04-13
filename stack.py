# last in first out

class Stack(object):
    def __init__(self):
        self.item=[]

    def push(self,ele):
        self.ele=ele
        # pushes element to last index and return type is none
        self.item.append(ele)
    def pop(self):
        # this will remove last element and return type is none  
        self.item.pop()
        pass
    def peek(self):
        # allow us to see the last element and return type is last item
        if self.item:
            return self.item[-1]
        else:
            return None
    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None
    def isempty(self):
        # checks stack is empty or not 
        if self.item== []:
            return True
        else:
            return False                           
if __name__=="__main__":
    stack=Stack()
    stack.push("1")
    stack.push("2")
    print(stack.size())
    print(stack.peek())
    stack.pop()
    print(stack.isempty())
    print(stack.size())
            