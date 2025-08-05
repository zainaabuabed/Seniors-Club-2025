from YB_Pcb_Car import YB_Pcb_Car
import time

robot = YB_Pcb_Car()

def spin_right(duration=1,speed=70):
    #Spin clockwise in place
    robot.Car_Spin_Right(speed, speed)
    time.sleep(duration)
    robot.Car_Stop()

def spin_left(duration=1,speed=70):
    #Spin counter-clockwise in place
    robot.Car_Spin_Left(speed, speed)
    time.sleep(duration)
    robot.Car_Stop()

try:
    #forward for 30 cm
    robot.Car_Run(50, 50)
    time.sleep(1.4)
    robot.Car_Stop()

    #left 90 degrees
    spin_left(0.65,70)
    
    #forward 60 cm
    robot.Car_Run(50, 50)
    time.sleep(2)
    
    #left 45 degrees
    spin_left(0.3,70)

    #forward 30 cm
    robot.Car_Run(50, 50)
    time.sleep(1.4)

    #right 90 degrees
    spin_right(0.6,70)

    #forward 30 cm
    robot.Car_Run(50, 50)
    time.sleep(1.4)
    
    # correct the direction to forward
    spin_left(0.33,70)
    
    #forward 40 cm
    robot.Car_Run(50, 50)
    time.sleep(1.7)
    
    #turn right to the direction of z3
    robot.Car_Right(50, 0)
    time.sleep(1)
    
    #forward te reach z3 completely
    robot.Car_Run(50, 50)
    time.sleep(1.4)

    robot.Car_Stop()

except KeyboardInterrupt:
    robot.Car_Stop()
    
finally:
    robot.Car_Stop()

    