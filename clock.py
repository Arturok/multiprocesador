import threading
from time import sleep

class clock:
    play = False
    stop = False
    cicle = True
    countCile = 0
    timeCicle = 1

    # Constructor
    def __init__(self, update):
        self.update = update
        threading.Thread.__init__(self)
    
    # Pause
    def pause(self):
        if (self.play):
            self.play = False
    
    # Go
    def go(self):
        if (not self.play):
            self.play = True

    # Run
    def run(self):
        while(not self.stop):
            if(self.play):
                self.cicle = not self.cicle
                self.countCile += 1
                self.update(self.countCile)
                sleep(self.timeCicle)
            else:
                sleep(self.timeCicle/2)