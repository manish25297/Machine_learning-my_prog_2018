""" string concepts  """




m="manish kumar singh"
print m[2:]
print m [:18]
print m[:78]
print m[1:10]
print m[0:18:2]
print len(m)
print m[-1]
print m[14:1:-2]


b= "prashant tiwari"
s= m+"\t"+b
print s


i=0
while(i< len(m)):
    print m[i],
    i=i+1
print"\n"


for j in b:
    print j,
