from add_tail import *
from Node import Node
from SinglyList import SinglyList

newlist = SinglyList()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

add_tail(newlist, a)
add_tail(newlist, b)
add_tail(newlist, c)
add_tail(newlist, d)
add_tail(newlist, e)

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

add_tail(thirdlist, first)
add_tail(thirdlist, second)
add_tail(thirdlist, third)
add_tail(thirdlist, fourth)
add_tail(thirdlist, fifth)
add_tail(thirdlist, sixth)
add_tail(thirdlist, seventh)

for item in thirdlist:
    print(item.c)
