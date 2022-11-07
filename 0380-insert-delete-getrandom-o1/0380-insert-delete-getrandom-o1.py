class RandomizedSet:

    def __init__(self):
        self.valueMap = {}
        self.indexes = []
        self.index = 0

    def insert(self, val: int) -> bool:
        if val in self.valueMap:
            return False
        self.valueMap[val] = self.index
        self.indexes.append(val)
        self.index += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueMap:
            return False
        lastVal, idx = self.indexes[-1], self.valueMap[val]
        self.indexes[idx], self.valueMap[lastVal] = lastVal, idx
        self.valueMap.pop(val)
        self.indexes.pop()
        self.index -= 1
        
        return True

    def getRandom(self) -> int:
        randInt = random.randint(0, self.index - 1)
        return self.indexes[randInt]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()