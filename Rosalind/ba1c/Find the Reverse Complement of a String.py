def ReverseComplement(s):
  ans = ""
  for x in s:
    if x == 'A':
      ans+= 'T'
    elif x == 'T':
      ans+= 'A'
    elif x == 'C':
      ans+= 'G'
    elif x == 'G':
      ans+= 'C'
  ans = ans[::-1]
  return ans
  
s = input()
print(ReverseComplement(s))
