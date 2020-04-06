#!/usr/bin/python3.7

"""The game that is played by lighting up all three lights on the board."""

import sys
import subprocess
from volume_controller import VolumeController
from time import sleep
from Ellie_Button import Ellie_Button
from music_player import music_player
from datetime import datetime

VOL_FILE = open("volume","r")
VOLUME = VOL_FILE.read()
VOL_FILE.close()
SETTING_VOLUME = False

subprocess.Popen("amixer -c 0 set PCM " + VOLUME + "%", shell=True)

###SETME
LED_pins = [12, 16, 20]
button_pins = [4,17,22]

class light_game:
    """Class for the actual game."""
    
    buttons = [None,None,None]
    
    def __init__(self):
        self.playing = True
        self.is_winning = False
        self.mp = music_player(self)
        for i in range(3):
            b = Ellie_Button(LED_pins[i],button_pins[i],False,self.mp,self)
            self.buttons[i] = b
        self.initialized = False

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
        self.initialized = True

    def check_buttons(self):
        if self.buttons[0].button.is_pressed and self.buttons[2].button.is_pressed:
            return True
        else:
            return False


def control_volume(light_game_instance, volume_control_instance):
    a = light_game_instance.buttons[0]
    b = light_game_instance.buttons[1]
    c = light_game_instance.buttons[2]
    a.is_lit = True
    b.is_lit = False
    c.is_lit = True
    for light in [a,b,c]:
        light.showlight()
    lg.playing = False
    vc.control_volume()

if __name__ == "__main__":
    lg = light_game()
    sleep(1)
    lg.startup()
    vc = VolumeController(lg)
    while True:
        try:
            if not lg.playing or not lg.initialized:
                continue
            if lg.buttons[0].button.held_time is None or lg.buttons[2].button.held_time is None:
                pass
            elif lg.buttons[0].button.held_time > 3 and lg.buttons[2].button.held_time > 3:
                control_volume(lg, vc)
                continue
            lg.check_win_condition()
        except KeyboardInterrupt:
            sys.exit(0)
