def HammingDistance(p,q):
  dis = 0
  for i in range(len(p)):
    if not p[i] == q[i]:
      dis+=1
  return dis
  
p = input()
q = input()

print(HammingDistance(p,q))
