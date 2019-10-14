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
    
def hamming_distance(a,b):
  length = len(a)
  cnt =0
  for x in range (length):
    if not a[x]==b[x]:
      cnt=cnt+1
  return cnt

genome = input()
d = input()
d = int(d)

lst = []
k_mers = []
all_possible_k_mers(len(genome),0,lst,k_mers)

for x in k_mers:
  if hamming_distance(x,genome) <= d:
    print(x)
