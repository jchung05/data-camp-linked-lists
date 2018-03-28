def has_cycle(player_list):
  itr = player_list.head
  for player in player_list:
    if itr.next:
      itr = itr.next.next
    if itr == player:
      return True
  return False
