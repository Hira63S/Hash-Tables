# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key             # key is to find which one is correct
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in s:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''

        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # we have key, value, and next
        new = self._hash(key) % self.capacity
        if self.storage[new] != None:      # if this hash not empty
            node = self.storage[new]       # we create a new node
            while node:
                if node.key == key:
                    node.value = value
                    break
                elif node.next == None:
                    node.next = LinkedPair(key, value)
                    break
                else:
                    node = node.next
        else:
            self.storage[new] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash(key) % self.capacity
        if self.storage[index] == None:
            print("ERROR: Key not found")
        if self.storage[index].next == None:
            if self.storage[index].key == key:
                self.storage[index].value = None
                return
            else:
                return('Key not found')
        while self.storage[index]:
            if self.storage[index].key == key:
                self.storage[index].value = None
                break
            self.storage[index] = self.storage[index].next

        return('Key not found')



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash(key) % self.capacity
        value = None
        if self.storage[index] != None:
            if self.storage[index].key == key:
                value = self.storage[index].value
                return value
            else:      # iterate
                self.storage[index] = self.storage[index].next
        else:
            print("Error: No values found")

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass
        # first thing to double the capacity:
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in self.storage:
            if i != None:
                index = i
                while index:
                    key = index.key
                    value = index.value
                    new = self._hash(key) % self.capacity
                    node = new_storage[new]
                    if node != None:
                        while node:
                            if node.next != None:
                                node = node.next
                            else:
                                node.next = LinkedPair(key, value)
                                node = None
                    else:
                        new_storage[new] = LinkedPair(key, value)

                    index = index.next

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
