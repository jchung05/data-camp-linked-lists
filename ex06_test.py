from trainyard import *
from Node import Node
from SinglyList import SinglyList

newlist = SinglyList()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(1019)

newlist.add_tail(a)
newlist.add_tail(b)
newlist.add_tail(c)
newlist.add_tail(d)
newlist.add_tail(e)
newlist.add_tail(f)

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

xxlist = trainyard(newlist, thirdlist)

for item in xxlist:
    print(item.c)
