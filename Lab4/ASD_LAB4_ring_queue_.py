class LIFO:
    def __init__(self):
        self.body = [0 for _ in range(12)]
        self.head = 6
        self.tail = 6
        self.size = 11

    def append(self, x):
        if self.head != self.tail + 1:
            self.body[self.tail] = x
            if self.tail != self.size:
                self.tail += 1
            else:
                self.tail = 0
        else:
            print("This queue is full")

    def output(self):
        if self.head != self.tail:
            x = self.body[self.head]
            if self.head != self.size:
                self.head += 1
            else:
                self.head = 0
            return x
        else:
            print("This queue is empty")

    def __str__(self):
        str_r = ""
        for i in range(12):
            if i == self.head:
                str_r += "Head -> "
            if i == self.tail:
                str_r += "Tail -> "
            str_r += f"{self.body[i]}\n"
        return str_r


cherg = LIFO()
print(cherg)
cherg.append(1)
print(cherg)
cherg.append(2)
cherg.append(3)
cherg.append(4)
cherg.append(5)
print(cherg)
cherg.append(6)
print(cherg)
cherg.append(7)
print(cherg)
cherg.append(8)
cherg.append(9)
cherg.append(10)
cherg.append(11)
cherg.append(12)
cherg.append(13)
print(cherg)
print("Queue out", cherg.output())
print(cherg)
cherg.output()
print(cherg)
cherg.output()
cherg.output()
cherg.output()
print(cherg)
cherg.output()
print(cherg)
cherg.output()
print(cherg)
cherg.output()
print(cherg)
cherg.output()
print(cherg)
cherg.output()
print(cherg)
cherg.output()
print(cherg)
cherg.output()
cherg.output()
cherg.output()
cherg.output()
print(cherg)
