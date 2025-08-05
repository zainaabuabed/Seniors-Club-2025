from YB_Pcb_Car import YB_Pcb_Car
import time

robot = YB_Pcb_Car()

robot.Ctrl_Servo(4, 90) #The servo connected to the S1 interface on the expansion board, rotate to 90°
time.sleep(0.5)
robot.Ctrl_Servo(4, 0) #The servo connected to the S1 interface on the expansion board, rotate to 90°
time.sleep(0.5)
robot.Ctrl_Servo(4, -90) #The servo connected to the S1 interface on the expansion board, rotate to 90°
time.sleep(0.5)