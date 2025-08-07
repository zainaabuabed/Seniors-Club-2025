from YB_Pcb_Car import YB_Pcb_Car
import time

robot = YB_Pcb_Car()

def spin_right(duration=1):
    #Spin clockwise in place
    robot.Car_Spin_Right(70, 70)
    time.sleep(duration)
    robot.Car_Stop()

def spin_left(duration=1):
    #Spin counter-clockwise in place
    robot.Car_Spin_Left(70, 70)
    time.sleep(duration)
    robot.Car_Stop()

try:
    # Move forward for 2 seconds
    robot.Car_Run(60, 60)
    time.sleep(2)
    
    # Stop for 2 seconds
    robot.Car_Stop()
    time.sleep(2)
    
    # Spin clockwise in place
    spin_right(1)  # 1 second for full rotation
    
    # Move backward for 2 seconds
    robot.Car_Back(60, 60)
    time.sleep(2)
    
    # Stop for 2 seconds
    robot.Car_Stop()
    time.sleep(2)
    
    # Spin counter-clockwise in place
    spin_left(1)  # 1 second for full rotation
    
    # Move forward for 2 seconds
    robot.Car_Back(60, 60)
    time.sleep(2)
    
    # Final stop
    robot.Car_Stop()

except KeyboardInterrupt:
   
    robot.Car_Stop()
     del robot  
finally: 
    robot.Car_Stop()
    del robot

    
