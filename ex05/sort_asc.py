def sortAsc(single_list):
  for itr in single_list:
    itr2 = itr.next
    while itr2:
      if itr2.content < itr.content:
        tmp = itr.content
        itr.content = itr2.content
        itr2.content = tmp
      itr2 = itr2.next
