import RPi.GPIO as GPIO
import time,sys
import requests
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()


URL = "http://avartan-env.pcw5e2rhtk.us-east-1.elasticbeanstalk.com/sendData"

FLOW_SENSOR = 22

#GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1
      #print count
      flow = (count*60 /7.5)
      #print(flow)

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)




while True:


	#ultrasonic sensor for distance
    TRIG = 23
    ECHO = 24
    print("Distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    print("Waitng for sensor")
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==False:
        pulse_start = time.time()
    while GPIO.input(ECHO)==True:
        pulse_end = time.time()
    pulse_duration=pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = int(distance, 2)
    print("Distance:",distance,"cm")

    #flow rate code to measure flowrate
    try:
        start_counter = 1
        time.sleep(0.2)
        start_counter = 0
        #flow = (count * 60 *60* 2.25 / 1000)
        flow = (count * 60 *60* 2 / 1000)
        #print(count)
        print "The flow is: %.0f Liter/min" % (flow)
        count = 0
        
        
       # PARAMS = {'dis':distance,'flow':flow}
        r = requests.post("http://avartan-env.pcw5e2rhtk.us-east-1.elasticbeanstalk.com/sendData"+"&dis="+distance+"&flow="+flow)
        
        #print(r.header)
        print(r.text)
        
        
        time.sleep(1)
    except KeyboardIntDerrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()




GPIO.cleanup()
