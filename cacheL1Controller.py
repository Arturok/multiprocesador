import cacheL1
class cacheL1Controller:
    hitRate = 0
    missRate = 0

    #Constructor
    def __init__(self, cacheL1, bus, state, update, coreID):
        self.cacheL1 = cacheL1
        self.bus = bus
        self.state = state
        self.update = update
        self.coreID = coreID

    # Mapping
    def mapBlock(self, block):
        cacheBlock = block
        add = 0
        while (cacheBlock >= self.cacheL1.size):
            cacheBlock -= self.cacheL1.size
            add += 1
        return cacheBlock, add

    # Pause
    def addPause(self, pause):
        self.thread_pause = pause

    # Read
    def read(self, block):
        cacheBlock, add = mapBlock(block)
        # Check if data is in cache
        cacheAdd = self.cacheL1.getAddress(cacheBlock)
        cacheState = self.cacheL1.getState(cacheBlock)
        miss = False
        if (cacheState == 'Invalid'):
            log = "$ CPU READ MISS VALID BLOCK: {}\n".format(hex(block))
            self.update_view(self.coreID, 'log', log=log)
            miss = True
        if (cacheState == 'Shared'):
            if (cacheAdd != add):
                log = "$ READ MISS ADD BLOCK: {}\n".format(hex(block))
                self.update_view(self.coreID, 'log', log=log)
        if (cacheState == 'Modified'):
            if(cacheAdd != add):
                miss = True
                # Write back
                data = self.cache.read(cacheBlock)

                log = "$ READ MIS"

    # Write
    #def write(slef):
    