
list1 = [1,1,1,2,2,2,1,1,1,4,4,4,5,5,6,3,3,4,3,7,7]
list2 = ["ben","ben","ga","ag","ga","ben","eoin","eoin","bla"]

def dedup_list2(li):
  a = len(li)
  c = 0
  li.sort()
  while c < a-1:
    if li[c] == li[c+1]:
      li.pop(c+1)
      a = a-1
    else:
      c = c+1

def deduplicate_list(li):
  d = {}
  for item in li:
	c = li.count(item)
	if c > 1:
	  d[item] = c
  for a in d:
    for b in range(d[a]-1): 
	  li.remove(a)

if __name__ == "__main__":
  dedup_list2(list1)
  print list1
  dedup_list2(list2)
  print list2