from time import sleep

class cacheL1:
    size = 2
    def __init__(self, coreID, update):
        self.update = update
        self.coreID = coreID
        self.readingDelayTime = 2
        self.writingDelayTime = 4
        self.data = {
        # block: [state, address data]
            0x0: ['invalid', '0000', '0000'],
            0x1: ['invalid', '0000', '0000']           
        }

        # Read in memory by block
        def readBlock(self, block):
            sleep(self.readingDelayTime)
            return self.data[block]

        # Write in memory by block
        def write(self, block, state, add, data):
            sleep(self.writingDelayTime)
            self.data[block] = [state, add, data]
            self.update(self.coreID, 'cache')

        # GETTERS
        # Get the state of a block
        def getState(self, block):
            return self.data[block][0]

        # Get the address of a block
        def getAddress(self, block):
            return self.data[block][1]

        # Get the blocks of the memory
        def getAddresses(self):
            return self.data.keys()

        # SETTERS
        # Set/update/change the state of a block
        def updateState(self, block, state):
            self.data[block][0] = state
            self.update(self.coreID, 'cache')


