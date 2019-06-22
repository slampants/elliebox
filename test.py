from light_game_gpiozero import light_game
from time import sleep

lg = light_game()
for light in lg.buttons:
    light.press()
    light.showlight()
sleep(1)
lg.check_win_condition()
