def count_occurance(a,b):
  length_a = len(a)
  length_b = len(b)

  i = 0
  cnt =0 
  while i+length_a <= length_b:
    if b[i:i+length_a]==a:
      cnt+=1
    i=i+1
  return cnt
  
def all_possible_k_mers(k,pos,lst,answer):
  flag = 0
  neucleotide = "ACGT"
  if pos == k:
    s=""
    for x in lst:
      s+=x
    answer.append(s)
    return
  for i in range (4):
    lst.append(neucleotide[i])
    all_possible_k_mers(k,pos+1,lst,answer)
    lst.pop()
    
genome = input()
k = input()
k = int(k)

k_mers = []
lst = []

all_possible_k_mers(k,0,lst,k_mers)

out = ""
for x in k_mers:
  out+= str(count_occurance(x,genome))+" "
  
print(out)
