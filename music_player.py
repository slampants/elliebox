import os
import atexit
from time import sleep
import pygame as pg
from random import randrange

SFX_PATH = "/home/pi/Desktop/elliebox/SFX/mp3/"
SFX_COUNT = 8


class music_player:
    """Music control."""

    def __init__(self):
        self.player = pg.mixer
        self.player.init(48000,-16,1,2048)
        self.clips = [""] * SFX_COUNT
        for number in range(1,SFX_COUNT):
            file_path = SFX_PATH + "elliebox_sfx_0" + str(number) + ".mp3"
            # print("Adding " + file_path + " to self.clips at index " + str(number))
            self.clips[number-1] = file_path
            # print("Item at self.clips[" + str(number) + "] is " + self.clips[number-1])
        self.clips[SFX_COUNT-1] = SFX_PATH + "elliebox_win.mp3"
        for item in self.clips:
            print(item)

    def load_and_play(self,path):
        print("Playing " + path)
        self.player.music.load(path)
        sleep(0.1)
        self.player.music.play()

    def play(self, win=False):
        """Play a sound clip.
        
        Args:
            win: Is this win condition?

        """
        if win:
            self.load_and_play(self.clips[SFX_COUNT])
        else:
            track = self.clips[randrange(0,SFX_COUNT-1)]
            self.load_and_play(track)
    
    def play_specific(self,num):
        """Play a specific sound clip.
        
        Args:
            num: The number of the file you want (must be between 1 and 7, inclusive)
        
        """
        track = self.clips[num-1]
        self.load_and_play(track)
        
    @atexit.register
    def kill_mixer(self):
        self.player.quit()