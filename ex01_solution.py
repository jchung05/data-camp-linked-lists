from Node import Node
from SinglyList import SinglyList

newlist = SinglyList()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

newlist.add_tail(a)
newlist.add_tail(b)
newlist.add_tail(c)
newlist.add_tail(d)
newlist.add_tail(e)

for item in newlist:
    print(item.c)

secondlist = SinglyList()

for item in secondlist:
    print(item.c)

thirdlist = SinglyList()
first = Node("My name is")
second = Node("Steve and this is")
third = Node("Jackbutt the movie")
fourth = Node("Warning graphic")
fifth = Node("content shown")
sixth = Node("Do not try this")
seventh = Node("at home")

thirdlist.add_tail(first)
thirdlist.add_tail(second)
thirdlist.add_tail(third)
thirdlist.add_tail(fourth)
thirdlist.add_tail(fifth)
thirdlist.add_tail(sixth)
thirdlist.add_tail(seventh)

for item in thirdlist:
    print(item.c)
