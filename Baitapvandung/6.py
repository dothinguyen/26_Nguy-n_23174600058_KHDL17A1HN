class Stack:
    def __init__(self, capacity=10):
        self.stack = [0.0] * capacity
        self.top = -1

    def push(self, item):
        if self.top < len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Ngăn xếp đã đầy.")

    def pop(self):
        return None if self.top == -1 else self.stack[self.top]

    def count(self):
        return self.top + 1

    def print_stack(self):
        if self.top == -1:
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp:", self.stack[:self.top + 1])

#-----------------------------------------------------------------------
stack = Stack(5)
stack.push(1.0)
stack.push(2.5)
stack.print_stack() 
print("Lấy ra:", stack.pop())
stack.print_stack() 
