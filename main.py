from screenController import ScreenController

screenCtrl = ScreenController()

def main():

    while True:
        input = raw_input(">: ")
        screenCtrl.handle(input)

if __name__ == '__main__':
    main()