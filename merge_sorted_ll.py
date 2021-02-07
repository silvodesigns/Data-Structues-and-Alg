def merge_sorted(self, llist):

  p = self.head 
  q = llist.head
  s = None

#Check for empty LinkedLists
  if not p:
      return q
  if not q:
      return p
#if not empty sets lower of two pointer as head of s
  if p and q:
      if p.data <= q.data:
          s = p 
          p = s.next
      else:
          s = q
          q = s.next
      new_head = s 
#while there are nodes on p and q:
  while p and q:
      if p.data <= q.data:
          s.next = p 
          s = p 
          p = s.next
      else:
          s.next = q
          s = q
          q = s.next
#if we reach none for either p, q or s, assign whatever is left to end of s
  if not p:
      s.next = q 
  if not q:
      s.next = p

  self.head = new_head     
  return self.head