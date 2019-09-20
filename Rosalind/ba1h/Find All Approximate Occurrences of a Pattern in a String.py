def HammingDistance(p,q):
  dis = 0
  for i in range(len(p)):
    if not p[i] == q[i]:
      dis+=1
  return dis
  
#pattern occurance with d hamming distance
def PatternOccurance(genome,pattern,d):
  i = 0
  ans = []
  while i+len(pattern) < len(genome):
    tmp_pattern = genome[i:i+len(pattern)]
    if HammingDistance(pattern,tmp_pattern)<=d:
      ans.append(i)
    i+=1
  return ans
  
pattern = input()
genome = input()
d = input()
d = int(d)

ans = PatternOccurance(genome,pattern,d)
out = ""

for x in ans:
  out+= str(x) + " "
  
print(out)
  
