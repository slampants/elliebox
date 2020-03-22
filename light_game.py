#!/usr/bin/python3.7

"""The game that is played by lighting up all three lights on the board."""

import sys
from time import sleep
from Ellie_Button import Ellie_Button
from music_player import music_player

###SETME
LED_pins = [12, 16, 20]
button_pins = [4,17,22]

class light_game:
    """Class for the actual game."""
    
    buttons = list()
    
    def __init__(self):
        self.is_winning = False
        self.mp = music_player(self)
        for i in range(3):
            b = Ellie_Button(LED_pins[i],button_pins[i],False,self.mp,self)
            self.buttons.append(b)

    def check_win_condition(self):
        """Poll each of the lights to see if they're on. If all three are on, run win method."""
        for light in self.buttons:
            if not light.is_lit:
                return
        self.win()
    
    def win(self):
        """Play win music, rotate through the lights which one should be on (ten total runthroughs), turn off all lights and kill the music."""
        self.is_winning = True
        sleep(0.5)
        self.mp.play(win=True)
        for i in range(6):
            for j in range(3): #Light up the lights one at a time
                for k in range(3): #Go through each light and only turn it on if it's the light in this cycle, otherwise turn it off
                    if j==k:
                        self.buttons[k].showlight(True)
                    else:
                        self.buttons[k].showlight(False)
                sleep(0.5)
        for light in self.buttons:
            light.is_lit = False
            light.showlight()
        self.is_winning = False
            
    def startup(self):
        """Light up the lights in order, play the specified 3 sound effects, turn lights off."""
        for i in range(3):
            self.buttons[i].light.on()
            self.buttons[i].showlight(True)
            self.buttons[i].mp.play_specific(i+1)
            sleep(0.5)
        sleep(2)
        for i in range(3):
            self.buttons[i].light.off()
            self.buttons[i].showlight()


if __name__ == "__main__":
    lg = light_game()
    sleep(1)
    lg.startup()
    while True:
        try:
            lg.check_win_condition()
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            lg.mp.player.quit()
