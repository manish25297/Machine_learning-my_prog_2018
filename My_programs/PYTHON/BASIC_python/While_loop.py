""" while loop"""


m="manish kumar singh"
ch="y"
  
j=17
while(j<25):
    print j
    j=j+1

    
while(ch=='y'):
    for i in range(0,18):
        print m[i],
    i+=1
    ch=raw_input(" \t enter x to stop")
    if ch=="x":
        break
    
    
