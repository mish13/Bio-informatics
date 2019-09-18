def FindOccurance(s,x):
  len_x = len(x)
  len_s = len(s)
  i = 0
  occurances = []
  while i+len_x <= len_s:
    if s[i:i+len_x] == x:
      occurances.append(i)
    i+=1
  return occurances
  
  
match = input()
given = input()

ans = FindOccurance(given,match)
out = ""
for x in ans:
  out = out + str(x) + " "
  
print(out)
