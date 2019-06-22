import gpiozero as gpio

class Ellie_Button:
    LED_pin = None
    button_pin = None
    is_lit = False
    light = None
    button = None
    
    def __init__(self,LEDpin,buttonPin,status):
        self.LED_pin = LEDpin
        self.button_pin = buttonPin
        self.button = gpio.Button(buttonPin)
        self.light = gpio.LED(LEDpin)
        self.button.when_pressed = self.press
        self.is_lit = status
        self.showlight()
        
    def press(self):
        self.is_lit = not self.is_lit
        self.showlight()
    
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
    
