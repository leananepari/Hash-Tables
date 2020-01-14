# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
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
        for x in key:
          hash = (( hash << 5) + hash) + ord(x)
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
        hash_k = self._hash_mod(key)

        if self.storage[hash_k] is not None:
          node = self.storage[hash_k]
          while True:
            if node.next is not None:
              node = node.next
            else:
              node.next = LinkedPair(key, value)
              break
        else:
          ll = LinkedPair(key, value)
          self.storage[hash_k] = ll



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_k = self._hash_mod(key)
        if self.storage[hash_k].key == key:
          return self.storage[hash_k].value
        elif self.storage[hash_k] is None:
          return None
        else:
          node = self.storage[hash_k]
          while True:
            if node.next.key == key:
              return node.next.value
            else:
              node = node.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")

ht = HashTable(8)
# print(ht.storage)
# ht.insert('key_1', 'value_1')
# ht.insert('key_2', 'value_2')
# print(ht.storage)
# print('GET', ht.retrieve('key_2'))

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")

print(ht.storage)