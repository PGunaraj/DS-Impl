# hash table

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, val):
        hashval = self.hashfunction(key, len(self.slots))  # get the hashvalue for the pair

        if self.slots[hashval] == None:  # enter the pair into hash table
            self.slots[hashval] = key
            self.data[hashval] = val
        else:
            if self.slots[hashval] == key:  # if key already present in the table, replace the val to new val
                self.data[hashval] = val
            else:  # current slot/position is filled, get the next empty slot
                nextslot = self.rehash(hashval, len(self.slots))
                while self.slots[nextslot] != None and self.slots[
                    nextslot] != key:  # when new slot is not either empty or key
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:  # found the next empty slot
                    self.slots[nextslot] = key
                    self.data[nextslot] = val
                else:  # found the next slot having key
                    self.data[nextslot] = val

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, hashval, size):
        return (hashval + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        pos = startslot
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20] = 'duck'
print(H[20])
print(H[99])

