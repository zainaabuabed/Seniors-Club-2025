from YB_Pcb_Car import YB_Pcb_Car
from Sensors import DistanceSensor, Buzzer
from time import sleep

robot = YB_Pcb_Car()
ultrasonic=DistanceSensor(18,16)
buzzer=Buzzer(32)

def openGate():
    for i in range(0,105,15):
        robot.Ctrl_Servo(4, i)
        sleep(0.5)
   
def closeGate():
    for i in range(90,-15,-15):
        robot.Ctrl_Servo(4, i)
        buzzer.beep()
        sleep(0.5)
        
     
robot.Ctrl_Servo(4, 0) 
gateState=False

try:
    while True:
        distance=ultrasonic.getDistance()
        sleep(1)
        if(distance<2):
            if(gateState==False):
                openGate()
                gateState=True
            elif(gateState==True):
                closeGate()
                gateState=False
                        
except KeyboardInterrupt:
    print("Ending")
finally:
    print("IO cleaned")
    ultrasonic.close()
    buzzer.close()


