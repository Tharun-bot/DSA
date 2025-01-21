class Queue:
    def __init__(self, size):
        self.top=-1
        self.bottom=-1
        self.size=size
        self.cuurent_size=0
        self.arr=[0]*self.size
    
    def push(self, value):
        if(self.top==-1 and self.bottom==-1):
            self.cuurent_size+=1
            self.top+=1
            self.bottom+=1
            self.arr[self.top]=value
        else:
            if(self.current_size<self.size):
                self.top=(self.top-1)%self.size
            self.arr[self.top]=value
            
