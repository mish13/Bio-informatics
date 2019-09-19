def LTClump(genome,k,l,t):
  genome_len = len(genome)
  ans = dict()
  
  i = 0
  while i+l < genome_len:
    clump = genome[i:i+l]
    occurance = dict()
    j = 0
    while j+k < l:
      k_mer = clump[j:j+k]
      if k_mer in occurance:
        occurance[k_mer]+=1
      else:
        occurance[k_mer] = 1
      j+=1
    for key,val in occurance.items():
      if val >= t:
        ans[key]=1
    i+=1
    
  return ans
  
genome = input()
k = input()
k = int(k)
l = input()
l = int(l)
t = input()
t = int(t)

out = ""
ans = LTClump(genome,k,l,t)
for key in ans:
  out+= key + " "
print(out)
