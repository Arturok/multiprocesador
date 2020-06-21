import cacheL1
import cacheL1Controller
import clock
import threading
import random
from time import sleep


class core:
    isa = ['read', 'write', 'calc']
    state = 'awake'

    class processor(threading.Thread):
        countInstructions = 1
        processTime = 1

        def __init__(self, coreID, chipID, clock, cacheL1, cacheL1Controller, update):
            self.coreID = coreID
            self.chipID = chipID
            self.clock = clock
            self.cacheL1 = cacheL1
            self.cacheL1Controller = cacheL1Controller
            self.standBy = threading.Condition()
            self.cacheL1Controller.addPause(self.standBy)
            self.update = update
            threading.Thread.__init__(self)

        def process(self):
            sleep(self.processTime)
            self.update(self.coreID, 'rates')

        def run(self):
            while(True):
                if(self.clock.play):
                    instruction = core.generateInstruction()
                    self.countInstructions += 1
                    command = "# Clicle: {} Instruction: {} ->\n {} ".format(self.clock.countCicle, self.countInstructions, instruction)
                    if (instruction in ['read', 'write']):
                        mainMemAdd = random.randrange(16)
                        command += "Address: {} CoreId: {} ChipId: {}".format(mainMemAdd, self.coreID, self.chipID)
                        self.update(self.coreID, 'log', log = command)

                        if(instruction == 'read'):
                            self.cacheL1Controller.rea
    
    # Core Constructor
    def __init__(self, coreID, chipID, clock, update):
        self.coreID = coreID
        self.chipID = chipID
        self.clock = clock
        self.update = update
    # Start
    def start(self):
        self.processor.start()

    # Get instruction
    @staticmethod
    def generateInstruction():
        # Special Distribution Function
        return core.isa[random.randrange(3)]

        
