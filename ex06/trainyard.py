def remove_last(single_list):
  for itr in single_list:
    if itr.next is None:
      itr = None

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
  while (train1 and train2):
    if train1 > train2:
      add_tail(newtrain, train1)
      train1 = train1.next
    else:
      add_tail(newtrain, train2)
      train2 = train2.next
  while train1:
    add_tail(newtrain, train1)
    train1 = train1.next
  while train2:
    add_tail(newtrain, train2)
    train2 = train2.next
  remove_last(newtrain)
  remove_last(newtrain)
  return newtrain
