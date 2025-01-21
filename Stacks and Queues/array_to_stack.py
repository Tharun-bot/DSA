class Stack:
    def __init__(self, size=1000):
        self.top = -1
        self.size=size
        self.arr = [0]*self.size
    
    def push(self, value):
        self.top+=1
        self.arr[self.top]=value

    def Top(self):
        if(self.top==-1):
            print('Nothing can be returned')
        else:
            return self.arr[self.top]
    
    def pop(self):
        if(self.top==-1):
            print('Nothing can be popped out')
        else:
            x = self.arr[self.top]
            self.top-=1
            return x
    def Size(self):
        return self.top+1
    
if __name__=="__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.Top())
    print("Size of stack before deleting any element", s.Size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.Size())
    print("Top of stack after deleting an element", s.Top())

            
    
        
