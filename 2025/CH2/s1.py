import YB_Pcb_Car as Raspbot
import time

robot=Raspbot.YB_Pcb_Car()

robot.Car_Run(70, 70)
time.sleep(5)

robot.Car_Stop()
time.sleep(2)

robot.Car_Back(70, 70)
time.sleep(5)

robot.Car_Stop()
