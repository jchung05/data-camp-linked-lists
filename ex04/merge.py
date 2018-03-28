def merge(train1, train2):
  newtrain = SinglyList()
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
  return newtrain
