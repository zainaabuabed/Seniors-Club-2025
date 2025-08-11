import YB_Pcb_Car    
from time import sleep

car = YB_Pcb_Car.YB_Pcb_Car()
car.Car_Run(30, 60)
sleep(3)
car.Car_Stop()