class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity  
        self.stack = [0.0] * capacity 
        self.top = -1  

    def push(self, item):
        if self.isFull():
            print("Ngăn xếp đã đầy.")
        else:
            self.top += 1
            self.stack[self.top] = item  

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
            return None
        item = self.stack[self.top]
        self.top -= 1  
        return item

    def isEmpty(self):
        return self.top == -1  

    def isFull(self):
        return self.top >= self.capacity - 1 

    def count(self):
        return self.top + 1  


# -------------------------------------------------------------------------------------
stack = Stack(5)  
stack.push(1.0)
stack.push(2.5)
stack.push(3.3)

print("Số phần tử trên ngăn xếp:", stack.count())  
print("Phần tử lấy ra:", stack.pop())  
print("Số phần tử trên ngăn xếp:", stack.count())  

