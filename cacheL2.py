from time import sleep

class cacheL2:
    size = 4
    def __init__(self, chipID, update):
        self.update = update
        self.chipID = chipID
        self.readingDelayTime = 3
        self.writingDelayTime = 6
        self.data = {
        # block: [state, owners, address, data]
            0x0: ['invalid', '', '0000', '0000'],
            0x1: ['invalid', '', '0000', '0000'],
            0x2: ['invalid', '', '0000', '0000'],
            0x3: ['invalid', '', '0000', '0000']
        }

        # Read in memory
        def read(self, block):
            sleep(self.readingDelayTime)
            return self.data[block][2]

        # Write in memory
        def write(self, block, state, owners, add, data):
            sleep(self.writingDelayTime)
            self.data[block] = [state, owners, add, data]
            self.update(self.chipID, 'cache')

        # Get the state of a block
        def getState(self, block):
            return self.data[block][0]

        # Get the owners of a block
        def getOwners(self, block):
            return self.data[block][1]

        # Get the address of a block
        def getAddress(self, block):
            return self.data[block][2]

        # Get the data of a block
        def getData(self, block):
            return self.data[block][3]
        
        # Get the blocks of the memory
        def getAddresses(self):
            return self.data.keys()

        # Set/update/change the state of an address
        def updateState(self, block, state):
            self.data[block][0] = state
            self.update(self.chipID, 'cache')

        # Set/update/change the owners of an address
        def updateOwners(self, block, owners):
            self.data[block][0] = owners
            self.update(self.chipID, 'cache')

