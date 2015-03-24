import sys,os

teststring = '{"ON":true,"color":"ffffff","deviceId":"1548"}'
pairs = teststring.split(',')
print pairs[0] 
print teststring[-6:-2]
