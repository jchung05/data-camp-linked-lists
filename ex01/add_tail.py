def add_tail(list_head, node):
  if list_head.head is None:
    list_head.head = node
  else:
    for item in list_head:
      current = item
    current.next = node
