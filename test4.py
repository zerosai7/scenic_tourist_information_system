import re
string=input()
result=re.search(re.compile('(.*?)/(.*)/(.*)'),string)
print(result)
print(result[1],result[2],result[3])