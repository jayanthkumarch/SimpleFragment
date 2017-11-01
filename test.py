import re

'''
string = 'Click here <h1 class="bigger">4 < 9</h1>'


regex = re.compile(r"<[^<]*>")
#regex = re.compile(r"<[^<]*?/?>")
print regex.sub('',string)
'''

fo = open("speedtest.txt","rb")
db = fo.read()
fo.close()
str1=""
print "just print",db

for i in db:
    str1+=i
print str1
