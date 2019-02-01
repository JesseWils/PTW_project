#!/usr/bin/python
import RPi.GPIO as GPIO
import time

while True:
    try:
          GPIO.setmode(GPIO.BOARD)

          PIN_TRIGGER = 7
          PIN_ECHO = 11

          GPIO.setup(PIN_TRIGGER, GPIO.OUT)
          GPIO.setup(PIN_ECHO, GPIO.IN)

          GPIO.output(PIN_TRIGGER, GPIO.LOW)

          print("Waiting for sensor to settle")

          time.sleep(2)

          print("Calculating distance")

          GPIO.output(PIN_TRIGGER, GPIO.HIGH)

          time.sleep(0.00001)

          GPIO.output(PIN_TRIGGER, GPIO.LOW)

          while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
          while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

          pulse_duration = pulse_end_time - pulse_start_time

          distance = round(pulse_duration * 17150, 2)
          procent = 100 - (int((100 / 300) * distance))
          print(procent)
          containerID = 1
          tijd = time.strftime('%a %d %B %H:%M:%S')
          list = [containerID, procent, tijd]
          print(list)
          # update de file met nieuwste meting
          with open('nieuwemeting.txt', 'w+') as myfile:
               myfile.write(str(list))
          print("Distance:", distance,"cm")

    finally:
          GPIO.cleanup()
      # wacht tot de volgende meting (tijd kan veranderd worden)
          time.sleep(3)
