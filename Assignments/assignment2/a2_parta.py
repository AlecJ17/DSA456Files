#    Main Author(s): 
#    Main Reviewer(s):

class HashTable:

    def __init__(self, cap=32):
        self.cap = cap
        self.size = 0
        self.table = [None] * self.cap
        self.tombstone = "tombstone"
        self.load_factor = 0.7

    def insert(self, key, value):
        idx = hash(key) % self.cap

        while self.table[idx] is not None:
            if self.table[idx][0] == key and self.table[idx] != self.tombstone:
                return False  # Key already exists
            idx = (idx + 1) % self.cap  # Move to the next index (linear probing)

        # Insert 
        self.table[idx] = (key, value)
        self.size += 1

        # Resize if the load factor exceeds 0.7
        if self.size / self.cap > self.load_factor:
            self.resize()
        return True
    def modify(self, key, value):
        idx=hash(key)%self.cap 
        orginal=idx
        while self.table[idx] is not None :
            if self.table[idx][0]==key and self.table[idx]!=self.tombstone:
                self.table[idx]=(key,value)
                return True
            idx=(idx+1)%self.cap
            if orginal==idx:
                break
        return False

    def remove(self, key):
        idx = hash(key) % self.cap
        start_index = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = self.tombstone
                self.size -= 1
                return True
            idx = (idx + 1) % self.cap
            if idx == start_index:
                break
        return False


    def search(self, key):
        idx = hash(key) % self.cap
        start_index = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.cap
            if idx == start_index:
                break
        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.size
    
    def resize(self):
        old_table = self.table
        self.cap *= 2
        self.table = [None] * self.cap
        self.size = 0
        
        # each item have key and value and insert back to table
        for item in old_table:
            if item is not None and item != self.tombstone:  # Check for None and tombstone
                key, value = item
                self.insert(key, value)

