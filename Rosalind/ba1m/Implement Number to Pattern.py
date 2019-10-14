rev_mapping = dict()

rev_mapping[0] = 'A'
rev_mapping[1] = 'C'
rev_mapping[2] = 'G'
rev_mapping[3] = 'T'

def Number_to_string(num,length):
  ret = ""
  while num>0:
    ret+=(rev_mapping[num%4])
    num//=4
    length-=1
  while length>0:
    ret+="A"
    length-=1
  ret = ret[::-1]
  return ret
  
num = input()
num = int(num)
length = input()
length = int(length)

print(Number_to_string(num,length))
