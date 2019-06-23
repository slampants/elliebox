#!/usr/bin/env python

"""The game that is played by lighting up all three lights on the board."""

from time import sleep
import subprocess
# import ButtonHandler
from Ellie_Button import Ellie_Button

###SETME
LED_pins = [16,20,21]
button_pins = [4,17,22]

class light_game:
    """Class for the actual game."""
    
    buttons = list()
    mp = None
    
    def __init__(self):
        self.mp = self.music_player()
        for i in range(3):
            b = Ellie_Button(LED_pins[i],button_pins[i],status=False)
            self.buttons.append(b)

    def push_button(self,button_index):
        """Change status of button's light boolean and change actual light accordingly.
        
        Args:
            light_index: The index number of the button that was pressed
            
        """
        self.lights[button_index][1] = not self.lights[button_index][1]
        print("Pressed button",button_index)
        self.mp.play()

    def check_win_condition(self):
        """Poll each of the lights to see if they're on. If all three are on, run win method."""
        for light in self.buttons:
            if not light.is_lit:
                return
        self.win()
    
    def win(self):
        """Play win music, rotate through the lights which one should be on (ten total runthroughs), turn off all lights and kill the music."""
        sleep(0.5)
        self.mp.play(0)
        for i in range(1): #TODO: Do ten times
            for j in range(3): #Light up the lights one at a time
                for k in range(3): #Go through each light and only turn it on if it's the light in this cycle, otherwise turn it off
                    if j==k:
                        self.buttons[k].showlight(True)
                    else:
                        self.buttons[k].showlight(False)
                sleep(1)
        for light in self.buttons:
            light.is_lit = False
            light.showlight()
        #Check whether the music has stopped playing


if __name__ == "__main__":
    lg = light_game()
    while True:
        try:
            lg.check_win_condition()
        except KeyboardInterrupt:
            exit()
