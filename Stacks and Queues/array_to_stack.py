from typing import List

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*self.size
        self.start = -1

    def push(self, value):
        if(self.start==self.size):
            print('Nothing can be added')
        else:
            self.start += 1
            self.arr[self.start] = value

    def pop(self):
        if(self.start==-1):
            print('Nothing can be removed')
        else:
            x = self.arr[self.start]
            self.start -= 1
            return x
    
    def Top(self):
        if(self.start==-1):
            print('Nothing on top')
        else:
            return self.arr[self.start]
    
    def Size(self):
        return self.start
    
if __name__ == "__main__":
    s = Stack(10)
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.Top())
    print("Size of stack before deleting any element", s.Size())
    print("The element deleted is", s.pop())
    print("Size of stack after deleting an element", s.Size())
    print("Top of stack after deleting an element", s.Top())


    



            
    
        
