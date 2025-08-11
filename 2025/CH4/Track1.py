import RPi.GPIO as GPIO
import time
from  YB_Pcb_Car import YB_Pcb_Car   

myCar = YB_Pcb_Car()

left1Sensor = 27   
left2Sensor = 22  
right1Sensor = 17  
right2Sensor = 4

direction =False   # False=> forward   True => backward
must_end=False     # False=>keep going  True=> must end path

def Hardware_Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(left1Sensor,GPIO.IN)
    GPIO.setup(left2Sensor,GPIO.IN)
    GPIO.setup(right1Sensor,GPIO.IN)
    GPIO.setup(right2Sensor,GPIO.IN)
    
def Read_Sensors():
    l1 = GPIO.input(left1Sensor) # left 1 sensor value
    l2= GPIO.input(left2Sensor)  # left 2 sensor value
    r1 = GPIO.input(right1Sensor) # right 1 sensor value
    r2 = GPIO.input(right2Sensor) # right 2 sensor value
    return[l1,l2,r1,r2]

def Spin_Counter_Clockwise(straightTime=1,spinTime=1):
    myCar.Car_Run(50, 50)
    time.sleep(straightTime)
    myCar.Car_Stop()
    myCar.Car_Spin_Left(70, 70)
    time.sleep(spinTime)

def Go_To_Tank():
    Sensors_Values=Read_Sensors()
    l1 = Sensors_Values[0]
    l2= Sensors_Values[1]
    r1 = Sensors_Values[2]
    r2 = Sensors_Values[3] 

    global direction
    global must_end

    # X 0 1 X      Handle a small left bend
    if l2==False and r1==True :
        myCar.Car_Spin_Left(40, 40) 
        time.sleep(0.02)
        
    # X 1 0 X      Handle the small right bend
    elif l2==True and r1==False:
        myCar.Car_Spin_Right(40, 40)
        time.sleep(0.02)
    
    # 0 0 0 1      Handle the cross while direction is forward
    elif l1==False and l2==False and r1==False and r2==True and direction==False:
        must_end=False
        print("Keep tracking => cross forward")

    # 1 0 0 0     Handle the cross while direction is back
    elif l1==True and l2==False and r1==False and r2==False and direction==True:
        must_end=True # the FireStation is near
        print("planing to end the path => cross back")
    
    # 0 0 0 0 handle all sensors inline
    elif l1==False and l2==False and r1==False and r2==False:
        if(direction==False):
            myCar.Car_Stop()
            time.sleep(2)  #stimulate filling the tank
            Spin_Counter_Clockwise(0.9,1) #straightTime=1.1 , spinTime=1
            direction=True  # direction now is back

    # 1 0 0 1 Processing straight lines        
    elif l1==True and l2==False and r1==False and r2==True:
	    myCar.Car_Run(50, 50) 
    
    # 1 1 1 1 handle all white => end of path
    elif l1==True and l2==True and r1==True and r2==True and direction==1:
        if(must_end==True):
            Spin_Counter_Clockwise(1.2,1.2) #straightTime=1.2 , spinTime=1.2
            return 0



Hardware_Setup()
try:
    while True:   
        End_Of_Path=Go_To_Tank()
        if End_Of_Path==0:
            print("end")
            break
     
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    myCar.Car_Stop() 
    