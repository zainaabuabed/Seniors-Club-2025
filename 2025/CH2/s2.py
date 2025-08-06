import YB_Pcb_Car as Raspbot
import time

robot=Raspbot.YB_Pcb_Car()

robot.Car_Run(60, 60)
time.sleep(3)

robot.Car_Stop()
time.sleep(2)

robot.Car_Right(50, 0)
time.sleep(1)

robot.Car_Run(60, 60)
time.sleep(3)

robot.Car_Stop()
time.sleep(2)

robot.Car_Back(60, 60)
time.sleep(3)

robot.Car_Left(0, 50)
time.sleep(1)

robot.Car_Run(60, 60)
time.sleep(2)

robot.Car_Stop()
del car
