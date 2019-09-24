class neucleotide_occurance:
  neucleotide = ""
  occurance = 0

def hamming_distance(a,b):
  length = len(a)
  cnt =0
  for x in range (length):
    if a[x]!=b[x]:
      cnt=cnt+1
  return cnt
 
def count_occurance(a,b,d):
  length_a = len(a)
  length_b = len(b)

  i = 0
  cnt =0 
  while i+length_a <= length_b:
    c = ""
    for j in range (length_a):
      c+=b[i+j]
    if hamming_distance(c,a) <= d:
      cnt = cnt+1
    i=i+1
  return cnt

def reverse_complement(a):
  b = ""
  length = len(a)
  for x in range (length):
    if a[x] == 'A':
      b+='T'
    elif a[x] == 'T':
      b+='A'
    elif a[x] == 'G':
      b+='C'
    elif a[x] == 'C':
      b+='G'
  return(b[::-1])
  
def all_possible_genome_sequence_with_reverse_complement(k,pos,lst,pattern,d,answer):
  flag = 0
  neucleotide = "ACGT"
  if pos == k:
    tmp = neucleotide_occurance()
    s=""
    for x in lst:
      s+=x
    tmp.neucleotide = s
    tmp.occurance = count_occurance(s,pattern,d)
    tmp.occurance += count_occurance(reverse_complement(s),pattern,d)
    answer.append(tmp)
    return
  for i in range (4):
    lst.append(neucleotide[i])
    all_possible_genome_sequence_with_reverse_complement(k,pos+1,lst,pattern,d,answer)
    lst.pop()
    
pattern = input()
k = input()
k = int(k)
d = input()
d = int(d)
mylist = []
ans = []
all_possible_genome_sequence_with_reverse_complement(k,0,mylist,pattern,d,ans)
mx_occur = -1
for x in ans:
  if x.occurance > mx_occur:
      mx_occur = x.occurance
out = ""
for x in ans:
  if x.occurance == mx_occur:
    out+=(x.neucleotide+" ")
print(out)
