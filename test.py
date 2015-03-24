import sys, time, serial,os

# script to test log redirect:
os.system('rm -rf pylog.txt')
os.system('touch pylog.txt') 
formerout=sys.stdout
sys.stdout = open('pylog.txt', 'w')
print 'test'
sys.stdout=formerout
logfile=open('pylog.txt', 'r')
jscon = str(logfile.readline())
logfile.close()
print jscon

print 'hello'
# now we grab the first line of the file. 

