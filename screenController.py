import screens
import Adafruit_CharLCD as LCD

class ScreenController(object):

    BUTTONS = ( (LCD.SELECT, currentScreen.btnUp),
                (LCD.LEFT,   currentScreen.btnLeft),
                (LCD.UP,     currentScreen.btnLeft),
                (LCD.DOWN,   currentScreen.btnLeft),
                (LCD.RIGHT,  currentScreen.btnLeft)
            )

    def __init__(self):
        self.currentScreenId = 0

        self.screens = [
            screens.AudioControl(screenCtrl=self),
            screens.Stock(screenCtrl=self)
        ]
        self.lcd = LCD.Adafruit_CharLCDPlate()
    

    
    def lcdLoop(self):
        buttons = ( (LCD.SELECT, self.currentScreen.btnUp),
                    (LCD.LEFT,   self.currentScreen.btnLeft),
                    (LCD.UP,     self.currentScreen.btnUp),
                    (LCD.DOWN,   self.currentScreen.btnDown),
                    (LCD.RIGHT,  self.currentScreen.btnRight)
            )

        for button in buttons:
            if self.lcd.is_pressed(button[0]):
                button[1]()
    
    def incrementScreen(self):
        newID = self.currentScreenId + 1
        self.currentScreenId = newID % len(self.screens)
        self.currentScreen.onDisplay()
    
    def decrementScreen(self):
        newID = self.currentScreenId - 1
        self.currentScreenId = newID % len(self.screens)
        self.currentScreen.onDisplay()
    
    def setScreen(self, id):
        self.currentScreenId = int(id)
        self.currentScreen.onDisplay()
    
    @property
    def currentScreen(self):
        return self.screens[self.currentScreenId]
