from base import Screen

class AudioControl(Screen):
    name = "Audio Control"
    color = "green"
    
    def btnUp(self):
        self.write("Hello World!")
    
    def onDisplay(self):
        self.write(self.name)
        self.setColor(self.color)
    
    def btnSelect(self):
        self.screenCtrl.incrementScreen()