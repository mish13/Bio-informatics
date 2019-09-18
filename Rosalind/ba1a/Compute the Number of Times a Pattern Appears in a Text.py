def Count(s,x):
  i = 0
  cnt = 0
  len_x = len(x)
  len_s = len(s)
  while i+len_x <= len_s:
    #print(s[i:i+len_x])
    if s[i:i+len_x] == x:
      cnt+=1
    i+=1
  return cnt
  
  given = input()
match = input()

print(Count(given,match))
