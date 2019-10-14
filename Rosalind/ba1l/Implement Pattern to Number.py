mapping = dict()

mapping['A']=0
mapping['C']=1
mapping['G']=2
mapping['T']=3

def String_to_number(s):
  mul = 1
  i = len(s)-1
  ans = 0
  while i>=0:
    ans+=(mapping[s[i]]*mul)
    mul*=4
    i-=1
  return ans
  
pattern = input()
print(String_to_number(pattern))
