import screens
import Adafruit_CharLCD

class ScreenController(object):

    def __init__(self):
        self.currentScreenId = 0

        self.screens = [
            screens.AudioControl(screenCtrl=self),
            screens.Stock(screenCtrl=self)
        ]
        self.lcd = Adafruit_CharLCD.Adafruit_CharLCDPlate()
    
    def handle(self, input):

        if input.lower() == "up":
            self.currentScreen.btnUp()
    
        if input.lower() == "down":
            self.currentScreen.btnDown()
        
        if input.lower() == "select":
            self.currentScreen.btnSelect()
    
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
