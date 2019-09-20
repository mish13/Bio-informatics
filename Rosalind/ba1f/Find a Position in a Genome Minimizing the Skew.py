def MinimizingSkew(s):
  mn = 1000000000
  cnt = 0
  skew = []
  ans = []
  for i in range(len(s)):
    if s[i] == 'C':
      cnt-=1
    elif s[i] == 'G':
      cnt+=1
    if cnt < mn:
      mn = cnt
    skew.append(cnt)
  for i in range(len(s)):
    if skew[i] == mn:
      ans.append(i+1)
  return ans
  
  genome = input()

ans = MinimizingSkew(genome)

out = ""
for x in ans:
  out+= str(x) + " "
  
print(out)
