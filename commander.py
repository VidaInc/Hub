import json
import pyserialcom
import time
import sys
import logger
import os

def changecolor(deviceID, Red, Green, Blue):
    red = deviceID + '014' + str(Red)
    green = deviceID + '015' + str(Green)
    blue = deviceID + '016' + str(Blue)
    r = sendMessage(red)
    time.sleep(2)
    g = sendMessage(green)
    time.sleep(2)
    b = sendMessage(blue)
    time.sleep(2)
    print 'result: ', r, g, b

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def sendMessage(msg):
    recordMessage(msg)
    return pyserialcom.arduisend(msg)

def recordMessage(msg):
    print msg

# return a tuple of r,g,b
def translate(hex_color):
    return (str(int(hex_color[0:2], 16)), str(int(hex_color[2:4], 16)), str(int(hex_color[4:6], 16)))

class Commander():
    def __init__(self):
        self.cmd = 1
        self.state = 'OFF'
        self.ac_state = 'OFF'
        self.iBeaonThreshold = -50
        self.temperature = 0
    def cmdLight(self):
        self.cmd = 1
    def cmdTemp(self):
        self.cmd = 1
    def turnLightON(self, deviceID):
        print 'Turn on light now'
        if self.state == 'ON':
            return 
        self.state = 'ON'
        sendMessage(deviceID + '011000')
    def turnLightOFF(self, deviceID):
        print 'Turn off light now'
        if self.state == 'OFF':
            return 
        self.state = 'OFF'
        sendMessage(deviceID + '010000')   
    def turnACON(self, deviceID):
        print 'Turn AC ON'
        if self.ac_state == 'ON':
            return 
        self.ac_state = 'ON'
        sendMessage(deviceID + '021000')  

    def turnACOFF(self, deviceID):
        print 'Turn AC OFF'
        if self.ac_state == 'OFF':
            return 
        self.ac_state = 'OFF'
        sendMessage(deviceID + '020000')

    def addTemperture(self, deviceID, temperature):
        print 'setTemperture' + str(temperature)
        sendMessage(deviceID + '024000')        

    def decTemperture(self, deviceID, temperature):
        print 'setTemperture' + str(temperature)
        sendMessage(deviceID + '025000')        
    # def parseCmd(self, device, deviceID, cmd):
    def parseCmd(self, device, cmd):
    	js = json.loads(cmd)
	print js
        	#print js.has_key('a')
        pyserialcom.arduiinit()
	# refresh the log file
	os.system('rm -rf pylog.txt')
	os.system('touch pylog.txt')
	formerout = sys.stdout
	sys.stdout = open("pylog.txt", 'w')
	print cmd
	# print js to std out to do string parsing. 
	sys.stdout = formerout
	# syslog is now redirected to stdout
	logfile=open('pylog.txt', 'r')
	jscmd = str(logfile.readline())
	logfile.close()
	print 'jscmd'
	print jscmd
	 
        if device == 'iBeacon':
	
	    '''
            for key in js:
                if str(key) == 'rssi':
                    if int(js[key]) >= self.iBeaonThreshold:
                        self.turnLightOn('2351')
			self.turnLightOn('2998')
                if str(key) == 'ON':
                    if str(js[key]) == 'true' or str(js[key]) == 'True':
                        if self.state == 'ON':
                            return      
                        #self.turnACON('2466')
                        #time.sleep(2)                        
                        #self.addTemperture('2466', str(js[key]))
                        #time.sleep(2)
                        self.turnLightON('2998')

                    if str(js[key]) == 'false' or str(js[key]) == 'False':
                        if self.state == 'OFF':
                            return 
                        self.turnLightOFF('2998')
		#if str(key) == 'temp':
	    '''		
			

        elif device == 'ac':
            print "ac json get"
            #pyserialcom.arduiinit()
            for key in js:
		if is_number(str(key)) == True:
		    deviceID = str(key)
		    print deviceID
            for key in js:
                if str(key) == 'ON':
                    if str(js[key]) == 'true' or str(js[key]) == 'True':
                        self.turnACON(deviceID)
                        
                    if str(js[key]) == 'false' or str(js[key]) == 'False':
                        self.turnACOFF(deviceID)

                if str(key) == 'Temperature':
                    if str(js[key]) == '-1':
                        continue
                    if int(js[key]) >= int(self.temperature):
                        self.addTemperture(deviceID, str(js[key]))
                    else:
                        self.decTemperture(deviceID, str(js[key]))
                    self.temperature = str(js[key])

                    


        elif device == 'light':
            print "light json get"
	    print "parsing json"
            deviceID = jscmd[-7:-3]
	    print deviceID
            if "ON" in jscmd:
                print 'light in key ON'
                if "true" in jscmd or "True" in jscmd:
                    self.turnLightON(deviceID)
                    
                if "false" in jscmd or "False" in jscmd:
                    self.turnLightOFF(deviceID)
	    '''
            if str(key) == 'color':
                if str(js[key]) == 'ffffff':
                    continue
                rgb_tuple = translate(js[key])
                c = [0 ,0 ,0]
                c[0] = rgb_tuple[0]
                c[1] = rgb_tuple[1]
                c[2] = rgb_tuple[2]
                for i in range(0, 3):
                    print i, 'ttttt'
                    if len(c[i]) == 1:
                        c[i] = '00' + c[i]
                    if len(c[i]) == 2:
                        c[i] = '0' + c[i]
                print 'ttttt'

                changecolor(deviceID, c[0], c[1], c[2])
            '''
            pyserialcom.arduireceive()
	elif device == 'door':
	    for key in js:
		if str(key) == 'LOCK':
		    print 'door will be locked'
		    # here we check local file for status
	            # lock door script. 
		if str(key) == 'OPEN':
		    print 'door will open'
		    # open door script.


        if js.has_key('Lock'):
        	print 'has lock: ', js['Lock']
        	if js['Lock'] == 'True' or js['Lock'] == 'true':
        		print 'Lock door'
        	if js['Lock'] == 'False' or js['Lock'] == 'false':
        		print 'Open door'
        elif js.has_key('Temperature'):
        	print 'Set Temperature'
        elif js.has_key('Color'):
            print 'Set Color'





def main():
    print 'ha'

if __name__ == '__main__':
    main()





