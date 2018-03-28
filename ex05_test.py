from sort_asc import *
from Node import Node
from SinglyList import SinglyList

newlist = SinglyList()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

newlist.add_tail(e)
newlist.add_tail(d)
newlist.add_tail(c)
newlist.add_tail(b)
newlist.add_tail(a)

sort_asc(newlist)

for item in newlist:
    print(item.c)

secondlist = SinglyList()

sort_asc(secondlist)

for item in secondlist:
    print(item.c)

thirdlist = SinglyList()
first = Node(76)
second = Node(93)
third = Node(11)
fourth = Node(1019)
fifth = Node(530)
sixth = Node(777)
seventh = Node(0)

thirdlist.add_tail(first)
thirdlist.add_tail(second)
thirdlist.add_tail(third)
thirdlist.add_tail(fourth)
thirdlist.add_tail(fifth)
thirdlist.add_tail(sixth)
thirdlist.add_tail(seventh)

sort_asc(thirdlist)

for item in thirdlist:
    print(item.c)
