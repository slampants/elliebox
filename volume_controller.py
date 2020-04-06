import subprocess
from time import sleep
from gpiozero import Button

class VolumeController:
    def __init__(self, game_instance):
        self.game = game_instance
        self.player = self.game.mp
        vol_file = open("volume","r")
        self.volume = int(vol_file.read())
        vol_file.close()
        self.button_down = self.game.buttons[0]
        self.button_exit = self.game.buttons[1]
        self.button_up = self.game.buttons[2]
        self.all_buttons = [self.button_down, self.button_exit, self.button_up]
        self.volume_isBeingControlled = False

    def set_volume(self):
        command = "amixer -c 0 set PCM " + str(self.volume) + "%"
        subprocess.Popen(command, shell=True)

    def volume_feedback(self):
        self.set_volume()
        self.player.play_specific(1)

    def volume_up(self):
        self.volume += 10
        if self.volume > 100:
            self.volume = 100
        self.volume_feedback()

    def volume_down(self):
        self.volume -= 10
        if self.volume < 0:
            self.volume = 0
        self.volume_feedback()

    def check_exit(self):
        held_time = self.button_exit.button.held_time
        if held_time is None:
            return
        elif held_time > 0:
            self.exit()

    def exit(self):
        self.volume_isBeingControlled = False
        VOL_FILE = open("volume","w")
        VOL_FILE.write(str(self.volume))
        VOL_FILE.close()
        for button in self.game.buttons:
            button.is_lit = False
            button.showlight()
        self.player.play_specific(2)
        sleep(0.1)
        self.player.play_specific(4)
        sleep(0.1)
        self.player.play_specific(6)
        sleep(0.1)
        self.player.StopAll()
        self.game.playing = True


    def control_volume(self):
        self.volume_isBeingControlled = True
        self.player.play_specific(6)
        sleep(0.1)
        self.player.play_specific(4)
        sleep(0.1)
        self.player.play_specific(2)
        sleep(0.1)
        self.player.StopAll()
        while self.button_down.button.is_pressed and self.button_up.button.is_pressed:
            sleep(0.25)
        while self.volume_isBeingControlled:
            self.check_exit()
            if self.button_down.button.is_pressed:
                while(self.button_down.button.is_pressed):
                    sleep(0.25)
                self.volume_down()
                sleep(0.25)
                continue
            elif self.button_up.button.is_pressed:
                while(self.button_up.button.is_pressed):
                    sleep(0.25)
                self.volume_up()
                sleep(0.25)
                continue
