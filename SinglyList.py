###########
#SINGLYLIST
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
    
  def print_list(self):
    for item in self:
        print(item.c)

  def add_head(self, node):
    if self.isEmpty():
      self.head = node
    else:
      node.next = self.head
      self.head = node

  def search(self, val):
    if (self.isEmpty()):
      return (False)
    for item in self:
      if (item.content == val):
        return (True)
    return (False)

  def add_tail(self, node):
    if (self.isEmpty()):
      self.head = node
    else:
      for item in self:
        current = item
      current.next = node
  
  def size(self):
    count = 0
    for _ in self:
      count += 1
    return (count)

  def remove(self, val):
    previous = None
    for item in self:
      if (item.content == val):
        if (previous):
          previous.next = item.next
          break
        else:
          self.head = item.next
      previous = item
      
  def cycles(self):
    itr = self.head
    for item in self:
      if (itr.next):
        itr = itr.next.next
      if (itr == item):
        return (True)
    return (False)
