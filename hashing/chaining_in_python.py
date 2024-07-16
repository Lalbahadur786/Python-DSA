# Make a class MyHash
# elements : 71, 49, 52, 63, 56, 50
# hash function x % Bucket size
class MyHash:
    def __init__(self, bucket_size):
        self.bucket_size = bucket_size
        self.hash_table = [[] for _ in range(bucket_size)]
    
    def get_hash(self, value):
        return value %  self.bucket_size
    
    def insert(self, value):
        index = self.get_hash(value)
        print(f"index: {index}")
        self.hash_table[index].append(value)
    
    def print_hash_table(self):
        print(self.hash_table)
    
    def search_value(self, value):
        index = self.get_hash(value)
        if value in self.hash_table[index]:
            return True
        return False
    
    def delete_value(self, value):
        index = self.get_hash(value)
        self.hash_table[index].remove(value)

myh = MyHash(7)
myh.print_hash_table()
myh.insert(71) #71, 49, 52, 63, 56, 50
myh.insert(49)
myh.insert(52)
myh.insert(56)
myh.insert(63)
myh.insert(56)
myh.insert(50)
myh.print_hash_table()
myh.delete_value(56)
myh.print_hash_table()
print(myh.search_value(52))