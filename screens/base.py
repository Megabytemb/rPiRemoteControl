class Screen(object):
    color = "White"

    def __init__(self, screenCtrl):
        self.screenCtrl = screenCtrl

    def handle(self, payload):
        raise NotImplementedError

    def btnLeft(self):
        raise NotImplementedError
    
    def btnRight(self):
        raise NotImplementedError
    
    def btnUp(self):
        raise NotImplementedError
    
    def btnDown(self):
        raise NotImplementedError
    
    def btnSelect(self):
        raise NotImplementedError
    
    def onDisplay(self):
        raise NotImplementedError
    
    def write(self, text):
        print "print: " + str(text)
    
    def setColor(self, color):
        print "color: " + str(color)
    