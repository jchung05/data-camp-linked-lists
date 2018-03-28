from Node import Node
from SinglyList import SinglyList

def remove_last(single_list):
  for itr in single_list:
    if itr.next is not None:
      prev = itr
  prev.next = None

def selectionSortDesc(single_list):
  for itr in single_list:
    itr2 = itr.next
    while itr2:
      if itr2.content > itr.content:
        tmp = itr.content
        itr.content = itr2.content
        itr2.content = tmp
      itr2 = itr2.next

def trainyard(train1, train2):
  newtrain = SinglyList()
  selectionSortDesc(train1)
  selectionSortDesc(train2)
  itr1 = train1.head
  itr2 = train2.head
  while (itr1 and itr2):
    if itr1.content > itr2.content:
      tmp = itr1
      itr1 = itr1.next
      tmp.next = None
    else:
      tmp = itr2
      itr2 = itr2.next
      tmp.next = None
    newtrain.add_tail(tmp)
  while itr1:
    tmp = itr1
    itr1 = itr1.next
    tmp.next = None
    newtrain.add_tail(tmp)
  while itr2:
    tmp = itr2
    itr2 = itr2.next
    tmp.next = None
    newtrain.add_tail(tmp)
  remove_last(newtrain)
  remove_last(newtrain)
  return newtrain

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
