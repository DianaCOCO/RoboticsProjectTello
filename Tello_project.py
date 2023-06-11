#!/usr/bin/python3
import time


import Tello
if __name__ == "__main__":
    tello = Tello.Controller()
    #Connect to the drone
    tello.send_command("command")
    time.sleep(2)
    #Takeoff
    tello.send_command("takeoff")
    time.sleep(5)
    #Creating Letter "L"
    #Move forward to create the vertical line of "L"
    tello.send_command("forward 100")
    time.sleep(2)
    #Rotate COUNTERclockwise to create the horzontal line of the "L"
    tello.send_command("ccw 90")
    time.sleep(2)
    #Move forward to create the vertical line of "L"
    tello.send_command("forward 100")
    time.sleep(2)
    #Creating letter "V"
    tello.send_command("ccw 45")
    time.sleep(2)
    tello.send_command("forward 100")
    time.sleep(2)
    tello.send_command("ccw 90")
    time.sleep(2)
    tello.send_command("forward 100")
    time.sleep(2)
    #Creating Letter "I"
    #Move forward to create the vertical line of "I"
    tello.send_command("forward 100")
    time.sleep(2)
    #Creating Number "3"
    #2 semicircles clockwise
    tello.send_command("curve 70 70 0 140 0 0 20")
    time.sleep(2)
    tello.send_command("curve 70 70 0 140 0 0 20")
    time.sleep(2)
    #Creating Number "5"
    tello.send_command("cw 90")
    time.sleep(2)
    tello.send_command("forward 100")
    time.sleep(2)
    tello.send_command("ccw 45")
    time.sleep(2)
    tello.send_command("forward 50")
    time.sleep(2)
    tello.send_command("curve 70 70 0 140 0 0 20")
    time.sleep(2)
    #Draw Number "7"
    tello.send_command("left 50")
    time.sleep(2)
    tello.send_command("ccw 45")
    time.sleep(2)
    tello.send_command("forward 100")
    time.sleep(2)
    tello.send_command ("land")
