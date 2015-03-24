import os
import commands

class RFcommunicator():
    def __init__(self):
        self.num = 1
        #self.queue = queue
    def send(self):
        os.system('ls -al')

def main():
    rf = RFcommunicator()
    #rf.send()
    str = os.popen("ls").read()
    print 'str: ', str
    os.system("top > temp.txt")

if __name__ == '__main__':
    main()