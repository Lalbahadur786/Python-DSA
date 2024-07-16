# Linear probing open addressing hash table
# No auxilary space or  linked list chaining required
# Main focus is to  fill all slots of hash  table
# Algorithm
#  step 1 : compute the hash of key
#           if collision occurs:
#               case 1 : next slot is available
#                      use next available slot
#               case 2 :  collided hash key is the last slot of hash table
#                      find next avaiable slot in circular fashion                       
#           else:
#               fill the slot of hash key

class linear_probe:

    def __init__(self, Bucket_size):
        self.size = 7
        self.hash_table = [-1] * self.size
      
    def insert(self, value):
        # we can check if value already present later
        hash_key = value % self.size
        # Linear probing
        # hash_key = (hash_key + 1) % size (hashsize)
        # for quadratic (elem + (counter**2)) % hashsize
        while self.hash_table[hash_key] != -1 and self.hash_table[hash_key] != value:
            hash_key = (hash_key + 1) % self.size
            if hash_key == value % self.size:
                break
        if self.hash_table[hash_key] == -1 or self.hash_table[hash_key] == value:
            self.hash_table[hash_key] = value
    def print_hash_table(self):
        print(self.hash_table)

arr = [70, 35, 52, 65, 37, 43, 40, 42]
li_obj = linear_probe(len(arr))
for elem in arr:
    li_obj.insert(elem)

li_obj.print_hash_table()