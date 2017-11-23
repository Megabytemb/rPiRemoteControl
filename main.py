from screenController import ScreenController

screenCtrl = ScreenController()

def main():

    while True:
        screenCtrl.lcdLoop()

if __name__ == '__main__':
    main()