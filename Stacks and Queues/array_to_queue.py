class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*size
        self.top = -1
        self.bottom = -1
        self.cur_size = 0

    def push(self, value):
        if(self.cur_size==self.size):
            print('No more elements can be added')
        if(self.top == -1):
            self.top, self.bottom = 0, 0
        else:
            self.top = (self.top+1)%self.size
        self.arr[self.top] = value
        self.cur_size+=1
    
    def pop(self):
        if(self.top == -1):
            print('No elements to remove')
        x = self.arr[self.bottom]
        if(self.cur_size==1):
            self.bottom, self.top = -1, -1
        else:
            self.bottom = (self.bottom+1)%self.size
        self.cur_size-=1
        return x
    
    def Top(self):
        if(self.bottom == -1):
            print('Nothing on top')
            exit(1)
        return self.arr[self.bottom]
    
    def Size(self):
        return self.cur_size
    
if __name__ == "__main__":
    q = Queue(10)
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.Top())
    print("The size of the queue before deletion", q.Size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.Top())
    print("The size of the queue after deleting an element", q.Size())

    
