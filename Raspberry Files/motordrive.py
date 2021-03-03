import RPi.GPIO as GPIO
import urllib2
import time  # Import the 'time' library.

GPIO.setmode(GPIO.BOARD)  # Use board pin numbering
GPIO.setup(5, GPIO.OUT)  # Setup GPIO Pin 5 to OUT
GPIO.setup(7, GPIO.OUT)  # Setup GPIO Pin 7 to OUT
GPIO.setup(8, GPIO.OUT)  # Setup GPIO Pin 8 to OUT
GPIO.setup(10, GPIO.OUT)  # Setup GPIO Pin 10 to OUT


def Forward():
    GPIO.output(5, True) 
    GPIO.output(7, False)
    GPIO.output(8, True)
    GPIO.output(10, False)

def Right():
    GPIO.output(5, False)
    GPIO.output(7, False)
    GPIO.output(8, True)
    GPIO.output(10, False)

def Left():
    GPIO.output(5, True)
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(10, False)

def Stop():
    GPIO.output(5, False)
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(10, True)

def Back():
    GPIO.output(5, False)
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(10, True)

	

true = 1
while(true):
                try:
                        response = urllib2.urlopen('https://lextor.azurewebsites.net/buttonStatus.php')
                        status = response.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args

                print status
                if status=='Forward':
                    print "Forward is Running"
                    Forward()
                elif status=='Back':
                    print "Back is Running"
                    Back()
                elif status=='Stop':
                     print "Back is Running"
                     Stop()
                elif status=='Right':
                     print "Stop is Running"
                     Right()
                elif status=='Left':
                     print "Stop is Running"
                     Left()
                GPIO.cleanup()

