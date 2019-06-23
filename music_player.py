import subprocess
import random

class music_player:
        """Music control."""
        sfx = 1
        p = None

        def play(self, win=False):
            """Play a sound clip.
            
            Args:
                clip: The index number of the clip to play

            """
            if win:
                print("Play win music")
            else:
                print("Play sound effect")
                cmd = "sudo omxplayer /home/pi/Desktop/elliebox/" + str(randint(0,sfx)) + ".mp3 &"                  # lays out the complete string that you'll pass to bash when you call the command as a subprocess   
                p = subprocess.Popen(cmd, shell=True)
            # Do some stuff to create a command to send to subprocess.Popen as self.p
            # Send the command
            # Wait for the duration of the clip
            self.stop()
            # Return exit code or something here so that the calling function knows it's done playing? Really just necessary for the "win" function
        
        def stop(self):
            print("stop clip")
            #~ self.p.terminate()
