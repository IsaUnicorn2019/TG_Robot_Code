

from app.Robot import Controller, Py_Hat, Check_Input
from app.Autonomous import Autonomous


from time import sleep
import os


def my_custom_autonomous(hat):
    auto = Autonomous(hat)

    # Takes a value and time

    
    #auto.forward(0.2, 0.5)
    auto.turn_right(0.7, .8, invert=True)
    auto.forward(0.8,1)
    auto.turn_left(0.7,.85, invert=True)
    auto.forward(0.8,5.5)
    auto.turn_left(0.7,0.85, invert=True)
    auto.forward(0.8,2.8)
    auto.turn_right(0.7, .8,    invert=True)
    #auto.forward(0.8,1)


    # nr_balls = 0
    # #first dispenser
    # while nr_balls < 10:
    #     print(nr_balls)
    #     auto.forward(0.2, 0.5)
    #     auto.backward(0.2,0.5)
    #     nr_balls = nr_balls + 1

    
    # auto.turn_left(0.5,1)     
    # auto.forward(0.8,2)
    # auto.turn_right(0.5,1)
 

    # nr_balls = 0
    # while nr_balls < 10:
    #     auto.forward(0.2, 0.5)
    #     auto.backward(0.2, 0.5)
    #     nr_balls = nr_balls + 1

    
    auto.stop()


def my_custom_teleop():
    #controller class
    controller = Controller()

    #  initialize Pi Hat
    hat = Py_Hat(address=96)
    
    while True:
        controller.event_get()
        # setup controls
        leftstick = controller.set_axis('leftstick')
        rightstick = controller.set_axis('rightstick')
        LT = controller.set_axis('LT')
        RT = controller.set_axis('RT')

         #Button press to run Autonomous
        
        if LT > .75:
            my_custom_autonomous(hat) 
        if RT > .9:
            print("2")
            hat.motor(0, -.4)
            hat.motor(1, .2)
            sleep(.3)
            hat.motor(0, .4)
            hat.motor(1, -.2)
            sleep(.3)


        # drivetrain examples
        if leftstick > .05 or leftstick < -.05:
            hat.motor(0, leftstick)
        else:
            hat.motor(0, .05)   
          
        if rightstick > .05 or rightstick < -.05:
            hat.motor(1, -rightstick)
        else:
            hat.motor(1, .05)

         #sleep for smooth loops
        sleep(.02)
        


if __name__ == "__main__":
    import os
    os.system("sudo pkill -9 -f RobotCode.py")
    my_custom_teleop()









