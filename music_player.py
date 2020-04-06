import os
import atexit
from time import sleep
import pygame as pg
from random import randrange

SFX_PATH = "/home/pi/Desktop/elliebox/SFX/signed_wav/"
SFX_COUNT = 7


class music_player:
    """Music control."""

    def __init__(self, game):
        self.game = game
        pg.mixer.pre_init(frequency=44100,size=-16,channels=8,buffer=2048)
        # pg.mixer.pre_init(44100,-16,1,2048)
        pg.init()
        mixer = pg.mixer
        self.clips = [pg.mixer.Sound] * SFX_COUNT
        for number in range(1,SFX_COUNT):
            file_path = SFX_PATH + "elliebox_sfx_0" + str(number) + ".wav"
            self.clips[number-1] = pg.mixer.Sound(file_path)
        pg.mixer.music.load(SFX_PATH + "elliebox_win.wav")

    def play(self, win=False):
        """Plays a sound clip, or plays win music if win=True."""
        if win:
            pg.mixer.music.play()
        else:
            if self.game.is_winning:
                return
            if pg.mixer.find_channel() is None:
                pg.mixer.find_channel(True).stop()
            track = self.clips[randrange(0,SFX_COUNT-1)]
            track.play(0)
    
    def play_specific(self,num):
        """Plays a specific sound clip.
        
        Args:
            num: The number of the file you want
        
        """
        if pg.mixer.find_channel() is None:
            pg.mixer.find_channel(True).stop()
        track = self.clips[num-1]
        track.play(0)

    def StopAll(self):
        pg.mixer.stop()

    # @atexit.register
    def quit(self):
        pg.mixer.quit()

