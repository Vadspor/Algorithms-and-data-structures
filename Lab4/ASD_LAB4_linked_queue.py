class Node:
    def __init__(self, info=None, prev=None, next=None):
        self.info = info
        self.prev = prev
        self.next = next
        if self.info != None:
            self.len = 0

    def __str__(self):
        return f"{self.info}"
    def Take(self):
        return f"{self.info}"


class LinkedList:
    def __init__(self, head=None, tail=None, len=0):
        self.len = len
        self.head = head
        self.tail = tail

    def __str__(self):
        node = self.head
        # str = "\n<<--[From head: "
        str = "\n<<--[None -> "
        while node != None:
            str += f"{node} -> "
            node = node.next
        # str += "None\nFrom tail: "
        # node = self.tail
        # while node != None:
        #     str += f"{node} -> "
        #     node = node.prev
        str += "None]-->>\n"
        return str


    def addLast(self, e):
        last = Node(e)
        if self.len == 0:
            self.head = last
            self.tail = last
        else:
            node = self.head
            # for i in range(self.len-1):
            while node.next != None:
                node = node.next
            last.prev = node
            node.next = last
            self.tail = last
        self.len += 1


    def takeFirst(self):
        if self.len == 0:
            print("Empty linked list")
            return None
        elif self.len == 1:
            take = self.head
            self.head = None
            self.tail = None
            self.len = 0
            return take.Take()
        else:
            first = self.head
            first.next.prev = None
            self.head = self.head.next
            self.len -= 1
            return first.Take()


cherg = LinkedList()
cherg.addLast(3)
print(cherg)
cherg.addLast(4)
print(cherg)
cherg.addLast(5)
print(cherg)
cherg.addLast(6)
print(cherg)
cherg.addLast(7)
print(cherg)
cherg.addLast(8)
print(cherg)

print(cherg.takeFirst())
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)
cherg.takeFirst()
print(cherg)




