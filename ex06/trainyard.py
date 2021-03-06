class SinglyList(object):
  def __init__(self):
    self.h = None
  
  def __iter__(self):
    current = self.head
    while current:
      yield current
      current = current.next
    
  @property
  def head(self):
    return self.h
    
  @head.setter
  def head(self, val):
    self.h = val

  def isEmpty(self):
    return self.head == None
    
  def add_head(self, node):
    if self.isEmpty():
      self.head = node
    else:
      node.next = self.head
      self.head = node

def add_tail(list_head, node):
  if list_head.head is None:
    list_head.head = node
  else:
    for item in list_head:
      current = item
    current.next = node

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
    add_tail(newtrain, tmp)
  while itr1:
    tmp = itr1
    itr1 = itr1.next
    tmp.next = None
    add_tail(newtrain, tmp)
  while itr2:
    tmp = itr2
    itr2 = itr2.next
    tmp.next = None
    add_tail(newtrain, tmp)
  remove_last(newtrain)
  remove_last(newtrain)
  return newtrain
