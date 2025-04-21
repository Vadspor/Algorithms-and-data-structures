import random
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


    def addFirst(self, e):
        node = Node(e)
        if self.len == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.len += 1


    def add(self, i, e):
        if i == 0:
            self.addFirst(e)
        elif i > self.len:
            self.addLast(e)
        elif self.len == 0:
            self.addLast(e)
        elif i <= self.len:
            no = self.head
            de = self.head.next
            for k in range(i-1):
                no = no.next
                de = de.next
            newnode = Node(e)
            newnode.prev = no
            newnode.next = de
            no.next = newnode
            de.prev = newnode
            self.len += 1


    def takeFirst(self):
        if self.len == 0:
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


    def takeLast(self):
        # node = self.head
        # for k in range(self.len-2):
        #     node = node.next
        # last = node.next
        # node.next = None
        if self.len == 0:
            return None
        elif self.len == 1:
            take = self.head
            self.head = None
            self.tail = None
            self.len = 0
            return take.Take()
        else:
            last = self.tail
            last.prev.next = None
            self.tail = self.tail.prev
            self.len -= 1
            return last.Take()


    def remove(self, i):
        if i == 0:
            self.takeFirst()
        elif i >= self.len:
            self.takeLast()
        elif self.len <= 1:
            self.head = None
            self.tail = None
            self.len = 0
            return None
        else:
            no = self.head
            de = no.next.next
            for k in range(i - 1):
                no = no.next
                de = de.next
            no.next = de
            de.prev = no
            self.len -= 1
            return de.Take()


    def set(self, i, e):
        if self.len == 0:
                return "The List is Empty. There is nothing to change."
        else:
            if i == 0:
                node = Node(e)
                se = self.head.next
                node.next = se
                se.prev = node
                self.head = node
            else:
                no = self.head
                de = self.head.next.next
                for k in range(i-1):
                    no = no.next
                    de = de.next
                node = Node(e)
                node.next = de
                node.prev = no
                no.next = node
                de.prev = node



    def get(self, i):
        if 0 <= i < self.len:
            get = self.head
            for k in range(i):
                get = get.next
            return get.info
        else:
            return None


    # def sort(self):
    #     for i in range(self.len):
    #         for j in range(i):
    #             if int(self.get(i)) < int(self.get(j)):
    #                 # print(i, self.get(i))
    #                 # print(j, self.get(j))
    #                 x = self.get(i)
    #                 self.remove(i)
    #                 self.add(j, x)
    #                 # print(self.head)
    #                 # print()
    #     return self.head


# a = Node(2)
# a.next = Node(7)
# a.next.next = Node(3)
# c = Node(2)
# c.next = a
# print(a)


# v = Node(1)
# L = LinkedList()
# L.head = v
# L.len = 1
# for i in range(2, 10):
#     v.next = Node(i)
#     v.next.prev = v
#     L.tail = v.next
#     v = v.next
#     L.len += 1

# print(L, L.len, sep="\n")
# L.addLast(10)
# print(L, L.len, sep="\n")
# L.addLast(11)
# print(L, L.len, sep="\n")
# L.addFirst(0)
# print(L, L.len, sep="\n")
# L.add(1, -100)
# print(L, L.len, sep="\n")
# print(L.takeFirst())
# print(L, L.len, sep="\n")
# print(L.takeLast())
# print(L, L.len, sep="\n")
# print(L.remove(5))
# print(L, L.len, sep="\n")
# L.set(8, 100)
# print(L, L.len, sep="\n")
# print(L.get(6))
#
# print()
#
# l = LinkedList()
# l.addLast(10)
# l.addLast(11)
# l.addFirst(-1)
# l.addFirst(0)
# l.add(2, -100)
# print(l, l.len)
# print(l.takeFirst())
# print(l, l.len)
# print(l.takeLast())
# print(l, l.len)
# print(l.remove(1))
# print(l, l.len)
# l.set(1, 100)
# print(l, l.len)
# print(l.get(1))
#
# list = LinkedList()
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# list.addLast(random.randint(-10, 10))
# print(list, list.len)
# # for i in range(list.len):
# #     print(i, list.get(i))
# # print()
# print(list.sort(), list.len)

fref = ["run", "gun", "fire", "boom", "speed", "car", "combine", "engine", "sun", "sunshine", "be", "was", "beat", "write", "grep", "cat", "cut", "flash", "more", "word", "lines"]

dict = LinkedList()

for i in range(len(fref)):
    exec(f"{fref[i]} = LinkedList()")
    for j in fref[i]:
        # print(j)
        exec(f"{fref[i]}.addLast(j)")
        # exec(f"print({fref[i]}.len)")
    exec(f"dict.addLast({fref[i]})")
    # exec(f"print({fref[i]})")


print(dict.len)


for i in range(dict.len):
    d = dict.get(i)
    # print(d)
    # print(d.len)
    # d.takeLast()
    # print(d)
    if d.len % 2 != 0:
        print(d)
        d.takeFirst()
        d.takeLast()
        print(d)
        d.addLast(",")
        print(d, "\n")


print(dict)







