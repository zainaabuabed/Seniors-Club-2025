from Sensors import DistanceSensor
from time import sleep
ultrasonic=DistanceSensor(18,16)
try:
    while True:
        print (ultrasonic.getDistance())
        sleep(1)
                        
except KeyboardInterrupt:
    print("Ending")
finally:
    print("IO cleaned")
    ultrasonic.close()
    del ultrasonic


