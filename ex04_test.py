from merge import *
from Node import Node
from SinglyList import SinglyList

newlist = SinglyList()
a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7)
e = Node(9)

newlist.head = e
e.next = d
d.next = c
c.next = b
b.next = a

newlist2 = SinglyList()
f = Node(2)
g = Node(4)
h = Node(6)
i = Node(8)
j = Node(10)

newlist2.head = j
j.next = i
i.next = h
h.next = g
g.next = f

newnewlist = merge(newlist, newlist2)

for item in newnewlist:
    print(item.c)

thirdlist = SinglyList()
first = Node(76)
second = Node(93)
third = Node(11)
fourth = Node(1019)
fifth = Node(530)
sixth = Node(777)
seventh = Node(0)

thirdlist.head = fourth
fourth.next = sixth
sixth.next = fifth
fifth.next = second
second.next = first
first.next = third
third.next = seventh

thirdlist2 = SinglyList()
one = Node(9999999)

thirdlist2.head = one
newthirdlist = merge(thirdlist, thirdlist2)
for item in newthirdlist:
    print(item.c)
