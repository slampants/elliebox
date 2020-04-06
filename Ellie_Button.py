import gpiozero as gpio
from music_player import music_player

class Ellie_Button:
    LED_pin = None
    button_pin = None
    is_lit = False
    light = None
    button = None
    mp = None    
    
    def __init__(self,LEDpin,buttonPin,status,player,game):
        self.game = game
        self.mp = player
        self.LED_pin = LEDpin
        self.button_pin = buttonPin
        self.button = gpio.Button(pin=buttonPin, bounce_time=0.05)
        self.light = gpio.LED(LEDpin)
        self.button.when_pressed = self.press
        self.is_lit = status
        self.showlight()
        
    def press(self):
        if self.game.is_winning or not self.game.playing:
            return
        self.is_lit = not self.is_lit
        self.showlight()
        self.mp.play()
    
    def showlight(self,status=None):
        if status is None:
            if self.is_lit:
                self.light.on()
            else:
                self.light.off()
        else:
            if status:
                self.light.on()
            else:
                self.light.off()
    
