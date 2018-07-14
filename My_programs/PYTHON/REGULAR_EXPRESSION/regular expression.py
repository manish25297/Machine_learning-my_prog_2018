import re
a=" my name is manish kumar singh"
str = 'an example word:cat!!'
match = re.search(r'man\w\w\w', a)      #The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without
#change which is very handy for regular expressions (Java needs this feature badly!). I recommend that you always write pattern strings with the 'r' just as a habit.
# If-statement after search() tests if it succeeded
if match:
    print 'found', match.group() ## 'found word:cat'
else:
    print 'did not find'

print "******"
match2="1"
match2 = re.search('man\w', a)
print match2.group()
print match2
