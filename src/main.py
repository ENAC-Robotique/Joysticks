import pygame
from pygame.joystick import Joystick
from enum import Enum
import time



class Axis(Enum):
    ROLL = 0
    PITCH = 1
    THROTTLE = 2

# class StateButton(Enum):
#     PAS_ENFONCER = 0
#     ENFONCER = 1
#     POUSSER = 2
#     RELACHER = 3


class JoystickEcal ():
    def __init__(self):
        self.joystick: Joystick = None
        self.buttons = []
        self.axis = []
    def __repr__(self):
        return f"{len(self.axis)} Axis: {self.axis} \t{len(self.buttons)} Buttons : {self.buttons}"

    def open(self):
        while (self.joystick == None):
            for event in pygame.event.get():
                if event.type == pygame.JOYDEVICEADDED:
                    self.joystick = pygame.joystick.Joystick(event.device_index)
                    self.axis = [self.axis_get_value(n) for n in range(self.joystick.get_numaxes())]
                    self.buttons = [self.button_get_value(n) for n in range(self.joystick.get_numbuttons())]
                    print(self.joystick)
                    print(self)
                    time.sleep(0.5)

    def button_get_value(self,n):
        return self.joystick.get_button(n)
    
    def axis_get_value(self,n):
        if n == Axis.ROLL.value:
            return round(self.joystick.get_axis(n),2)
        else:
            return -round(self.joystick.get_axis(n),2)

    def update_value(self):
        for n in range(self.joystick.get_numbuttons()):
            self.buttons[n] = self.button_get_value(n)

        for n in range(self.joystick.get_numaxes()):
            self.axis[n] = self.axis_get_value(n)
        


pygame.init()
pygame.joystick.init()

baton_de_joie = JoystickEcal()        
baton_de_joie.open()



while True :
    for event in pygame.event.get():
        baton_de_joie.update_value()
        print(baton_de_joie)
    time.sleep(0.1)
    

