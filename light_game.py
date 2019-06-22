#!/usr/bin/env python

"""The game that is played by lighting up all three lights on the board."""

import RPi.GPIO as GPIO
from time import sleep
import subprocess
import ButtonHandler

###SETME
pins = [0,0,0]

class light_game:
    """Class for the actual game."""
    lights = ((11,False),(12,False),(21,False))
    mp = None
    bh = ButtonHandler(pin, misterManager, edge='rising', bouncetime=100)      # this sets up an instance of the ButtonHandler class for debouncing
    
    def __init__(self):
        try:
            
            for i in range(3):
                if pins[i] == 0:
                    raise Exception
            self.mp = music_player()
            self.lights = ((pins[0],False),(pins[1],False),(pins[2],False))
        except Exception:
            print("One or more of your pins in light_game is set to 0!\n")

    #TODO: This needs attention!
    class music_player:
        """Music control."""

        p = None

        def play(self, clip):
            """Play a sound clip.
            
            Args:
                clip: The index number of the clip to play

            """
            # Do some stuff to create a command to send to subprocess.Popen as self.p
            # Send the command
            # Wait for the duration of the clip
            self.stop()
            # Return exit code or something here so that the calling function knows it's done playing? Really just necessary for the "win" function
        
        def stop(self):
            self.p.terminate()




    

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
        for light in self.lights:
            if light[1] == False:
                return
        self.win()
    
    def win(self):
        """Play win music, rotate through the lights which one should be on (ten total runthroughs), turn off all lights and kill the music."""
        self.mp.play(0)
        for i in range(10): #Do ten times
            for j in range(3): #Light up the lights one at a time
                for k in range(3): #Go through each light and only turn it on if it's the light in this cycle, otherwise turn it off
                    if j==k:
                        GPIO.output(k,True)
                    else:
                        GPIO.output(k,False)
                sleep(1)
        for i in range(3):
            GPIO.output(lights[i][1],False) #Turn 'em all off
        #Check whether the music has stopped playing

lg = light_game()
