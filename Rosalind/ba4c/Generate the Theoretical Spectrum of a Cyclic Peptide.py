m = dict()

m['G']=57
m['A']=71
m['S']=87
m['P']=97
m['V']=99
m['T']=101
m['C']=103
m['I']=113
m['L']=113
m['N']=114
m['D']=115
m['K']=128
m['Q']=128
m['E']=129
m['M']=131
m['H']=137
m['F']=147
m['R']=156
m['Y']=163
m['W']=186

def FindWeight(s):
  wt = 0
  for i in range(len(s)):
    wt+=m[s[i]]
  return wt
  
peptide = input()

ans = []

ans.append(0)

l = 1

while l< len(peptide):
  start=0
  for k in range(len(peptide)):
    tmp = ""
    p = start
    koyta = 0
    while koyta < l:
      tmp += peptide[p]
      koyta+=1
      p+=1
      p%=len(peptide)
    ans.append(FindWeight(tmp))
    start+=1
  l+=1
ans.append(FindWeight(peptide))
ans.sort()
out = ""
for x in ans:
  out+= str(x)+" "
print(out)
