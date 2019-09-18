def FrequentWords(s,k):
  i = 0
  len_s = len(s)
  k_mer_occurances = dict()
  mx = -1
  ans = []
  while i+k <= len_s:
    k_mer = s[i:i+k]
    if k_mer in k_mer_occurances:
      k_mer_occurances[k_mer]+=1
      if k_mer_occurances[k_mer] > mx:
        mx = k_mer_occurances[k_mer]
    else:
      k_mer_occurances[k_mer]=1
      if k_mer_occurances[k_mer] > mx:
        mx = k_mer_occurances[k_mer]
  
    i+=1
    
  for k_mer in k_mer_occurances:
    if k_mer_occurances[k_mer] == mx:
      ans.append(k_mer)
  ans.sort()
  return ans
  
genome_sequence = input()
k = input()
k = int(k)

ans = FrequentWords(genome_sequence,k)

out = ""
for x in ans:
  out = out + x + " "
print(out)
