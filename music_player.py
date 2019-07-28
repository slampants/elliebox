import subprocess
from random import randrange

class music_player:
    """Music control."""
    sfx = 7

    def play(self, win=False):
        """Play a sound clip.
        
        Args:
            win: Is this win condition?

        """
        if win:
            cmd = "omxplayer -o alsa /home/pi/Desktop/elliebox/SFX/elliebox_win.wav &"
            p = subprocess.Popen(cmd, shell=True)
        else:
            cmd = "omxplayer -o alsa /home/pi/Desktop/elliebox/SFX/elliebox_sfx_0" + str(randrange(1,self.sfx+1)) + ".wav &"
            p = subprocess.Popen(cmd, shell=True)
            
    def play_specific(self,num):
        """Play a specific sound clip.
        
        Args:
            num: The number of the file you want (must be between 1 and 7, inclusive)
        
        """
        cmd = "omxplayer -o alsa /home/pi/Desktop/elliebox/SFX/elliebox_sfx_0" + str(num) + ".wav &"
        p = subprocess.Popen(cmd, shell=True)
