import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import the 'time' library.
import urllib2                 
def scan():
    GPIO.setmode(GPIO.BOARD)
    TRIG = 23                                  #Associate pin 23 to TRIG
    ECHO = 24                                  #Associate pin 24 to ECHO
    GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    print "Waitng For Sensor To Settle"
    time.sleep(2)                            #Delay of 2 seconds

    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
     pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
     pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points
    fdistance = distance - 0.5
    strdistance = str(fdistance)

    if distance > 2 and distance < 400:      #Check whether the distance is within range
     print "Distance:", fdistance, "cm"  #Print distance with 0.5 cm calibration
     file = open("sonicread.txt", "w")
     file.write(strdistance)
    else:
     print "Out Of Range"                   #display out of range
     file = open("sonicread.txt", "w")
     file.write("Out of Range")                   #display out of range
true = 1
while(true):
                try:
                        response = urllib2.urlopen('https://lextor.azurewebsites.net/ultrasonicStatus.php')
                        status = response.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args

                print status
                if status=='scan':
                    print "Ultrasonoc is Running"
                    scan()
                GPIO.cleanup()
