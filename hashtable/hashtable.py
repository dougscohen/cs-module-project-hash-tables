# import sys
# sys.path.append('C:\\Users\\dougcohen\\Repos\\CS\\cs-module-project-hash-tables')  # Adds higher directory to python modules path.

# from linked_list import LinkedList


from linked_list import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        
        self.storage = [LinkedList()] * capacity
        self.capacity = capacity
        self.number_of_records = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.number_of_records / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)
            
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # get the index into the hash table to store "value"
        index = self.hash_index(key)
        cur = self.storage[index].head
        
        while cur:
            if cur.key == key:
                cur.value = value
                
            cur = cur.next
        
        entry = HashTableEntry(key, value)
        self.storage[index].insert_at_head(entry)
        self.number_of_records += 1
        
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # # Find the index of the given key in the table
        # i = self.hash_index(key)
        
        # # Store its value to be returned later
        # deleted_value = self.table[i]
        
        # # Switch value at that index location to "None"
        # self.table[i] = None
        
        # return deleted_value
        
        self.put(key, None)
        self.number_of_records -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.


        Returns None if the key is not found.

        Implement this.
        """
        # Find the index of the given key in the table
        index = self.hash_index(key)
        cur = self.storage[index].head
        
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
            
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        if self.get_load_factor() >= 0.7:
            old_storage = self.storage
            self.storage = [LinkedList()] * new_capacity
            for record in old_storage:
                cur = record.head
                while cur:
                    self.put(cur.key, cur.value)
                    cur = cur.next
                    
            self.capacity = new_capacity

# ht = HashTable(8)
# ht.put('Doug', 28)
# print(ht.storage[0].head.key)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    
    # print(ht.get('line_2'))
    # print(ht.get('line_5'))
    # print(ht.get('line_8'))


    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
