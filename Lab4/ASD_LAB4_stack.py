class FIFO:
    def __init__(self):
        self.body = [None for _ in range(12)]
        self.head = 5
        self.tail = 5
        self.size = 11

    def __str__(self):
        str_r = ""
        for i in range(12):
            if i == self.head:
                str_r += "Head -> "
            if i == self.tail:
                str_r += "Tail -> "
            str_r += f"{self.body[i]}\n"
        return str_r

    def push_head(self, x):
        if self.head != self.size:
            self.head += 1
            self.body[self.head] = x
        else:
            print("Stack head is full")

    def push_tail(self, x):
        if self.tail != 0:
            if self.body[self.tail] != None:
                self.tail -= 1
            self.body[self.tail] = x
        else:
            print("Stack tail is full")

    def pop_head(self):
        if self.head != self.tail:
            x = self.body[self.head]
            self.head -= 1
            return x
        else:
            print("Stack is empty")

    def pop_tail(self):
        if self.tail != self.head:
            x = self.body[self.tail]
            self.tail += 1
            return x
        else:
            self.body[self.tail] = None
            print("Stack is empty")


stack = FIFO()
print(stack)
stack.push_head(1)
print(stack)
stack.pop_head()
print(stack)
stack.push_tail(2)
print(stack)
stack.push_head(3)
print(stack)
stack.push_tail(4)
stack.push_head(5)
stack.push_tail(6)
print(stack)
stack.push_head(7)
print(stack)
stack.push_tail(8)
print(stack)
stack.push_head(9)
print(stack)
stack.push_tail(10)
stack.push_head(11)
stack.push_tail(12)
stack.push_head(13)
stack.push_tail(14)
print(stack)

print(stack.pop_head())
print(stack)
print(stack.pop_tail())
print(stack)
stack.pop_head()
print(stack)
stack.pop_tail()
print(stack)
stack.pop_head()
stack.pop_tail()
print(stack)
stack.pop_head()
stack.pop_tail()
stack.pop_head()
stack.pop_tail()
stack.pop_head()
stack.pop_tail()
stack.pop_head()
stack.pop_tail()
stack.pop_head()
stack.pop_tail()
stack.pop_head()
print(stack)


stack.push_head(1)
print(stack)
stack.push_tail(2)
stack.push_head(3)
print(stack)
stack.push_tail(4)
stack.push_head(5)
stack.push_tail(6)
print(stack)
stack.push_head(7)
print(stack)
stack.push_tail(8)
print(stack)
stack.push_head(9)
print(stack)
stack.push_tail(10)
stack.push_head(11)
stack.push_tail(12)
stack.push_head(13)
stack.push_tail(14)
print(stack)


