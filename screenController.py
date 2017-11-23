import screens
import Adafruit_CharLCD as LCD

class ScreenController(object):

    def __init__(self):
        self.currentScreenId = 0

        self.screens = [
            screens.AudioControl(screenCtrl=self)
        ]
        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.previousBtnState = None
    
    def lcdLoop(self):

        if self.btnState != self.previousBtnState:
            if self.btnState[LCD.SELECT]:
                self.currentScreen.btnSelect()
            
            elif self.btnState[LCD.LEFT]:
                self.currentScreen.btnLeft()

            elif self.btnState[LCD.UP]:
                self.currentScreen.btnUp()
            
            elif self.btnState[LCD.DOWN]:
                self.currentScreen.btnDown()

            elif self.btnState[LCD.RIGHT]:
                self.currentScreen.btnRight()
            

            self.previousBtnState = self.btnState
    
    @property
    def btnState(self):
        return [
            self.lcd.is_pressed(LCD.SELECT),
            self.lcd.is_pressed(LCD.RIGHT),
            self.lcd.is_pressed(LCD.DOWN),
            self.lcd.is_pressed(LCD.UP),
            self.lcd.is_pressed(LCD.LEFT),
        ]

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
