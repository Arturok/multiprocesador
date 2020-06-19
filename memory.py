from time import sleep

class memory:
    size = 16
    def __init__(self, update):
        self.update = update
        self.readingDelayTime = 4
        self.writingDelayTime = 8
        self.data = {
        # block: [state, owners, data]
            0x0: ['invalid', '', '0000'],
            0x1: ['invalid', '', '0000'],
            0x2: ['invalid', '', '0000'],
            0x3: ['invalid', '', '0000']
        }
        # Read in memory
        def read(self, block):
            sleep(self.readingDelayTime)
            return self.data[block]

        # Write in memory
        def write(self, block, state, owners, data):
            sleep(self.writingDelayTime)
            self.data[block] = [state, owners, data]
            self.update(self)

        # GETTERS
        # Get the state of a block
        def getState(self, block):
            return self.data[block][0]

        # Get the ownners of a block
        def getOwners(self, block):
            return self.data[block][1]

        # Get the data of a block
        def getData(self, block):
            return self.data[block][2]


        # SETTERS
        # Set/update/change the state of a block
        def updateState(self, block, state):
            self.data[block][0] = state
            self.update(self)
