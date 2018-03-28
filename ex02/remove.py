def remove(list_head, val):
  previous = None
  for item in list_head:
    if item.content == val:
      if previous:
        previous.next = item.next
        break
      else:
        list_head.head = item.next
    previous = item
