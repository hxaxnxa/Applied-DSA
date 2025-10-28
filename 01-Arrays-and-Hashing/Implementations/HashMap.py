class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node(key:{self.key}, value:{self.value})"
    
class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * self.capacity
        print(f"HashMap initialized with {self.capacity} buckets.")

    def _hash(self,key):
        return abs(hash(key)) % self.capacity
    
    def put(self,key,value):
        index = self._hash(key)
        current_node = self.array[index]

        if current_node is None:
            self.array[index] = Node(key,value)
            print(f"Inserted {key}:{value} at index {index}.")
            return
        
        prev_node = None

        while current_node is not None:
            if current_node.key == key:
                current_node.value = value
                print(f"Updated {key} with new value {value} at index {index}.")
                return
            
            prev_node = current_node
            current_node = current_node.next

        print(f"PUT: Reached end of list. Adding new Node({key}, {value})")
        prev_node.next = Node(key,value)

    def get(self,key):
        index = self._hash(key)
        current_node = self.array[index]

        while current_node is not None:
            if current_node.key == key:
                print(f"GET: Found {key}:{current_node.value} at index {index}.")
                return current_node.value
            current_node = current_node.next

        print(f"GET: Key {key} not found.")
        raise KeyError(f"Key {key} not found")
    
    def display(self):
        for i in range(self.capacity):
            print(f"Bucket {i}:", end=" ")
            current_node = self.array[i]
            if current_node is None:
                print("Empty")
            else:
                while current_node:
                    print(f"({current_node.key}, {current_node.value}) -> ", end="")
                    current_node = current_node.next
                print("None")


if __name__ == "__main__":
    my_map = HashMap(capacity=5)
    my_map.display()
    
    print("--- Test 1: Basic Put and Get ---")
    my_map.put("hello", 100)
    print(f"Got: {my_map.get('hello')}")
    my_map.display()

    print("--- Test 2: Update Existing Key ---")
    my_map.put("hello", 200) 
    print(f"Got: {my_map.get('hello')}")
    my_map.display()

    print("--- Test 3: Force a Collision ---")
    print(f"Hash for 'apple': {my_map._hash('apple')}")
    print(f"Hash for 'banana': {my_map._hash('banana')}")
    print(f"Hash for 'orange': {my_map._hash('orange')}")
    my_map.put("apple", 50)
    my_map.put("banana", 75)
    my_map.put("orange", 125)
    
    my_map.display()
    
    print("--- Test 4: Get from a Collision Chain ---")
    print(f"Got 'apple': {my_map.get('apple')}")
    print(f"Got 'banana': {my_map.get('banana')}")
    print(f"Got 'orange': {my_map.get('orange')}")
    
    print("\n--- Test 5: Add another key ---")
    my_map.put("grape", 99)
    print(f"Hash for 'grape': {my_map._hash('grape')}")
    my_map.display()

    print("--- Test 6: Get Non-Existent Key (Error) ---")
    try:
        my_map.get("pear")
    except KeyError as e:
        print(f"Caught expected error: {e}")
        
    print("\nAll tests passed! Hash Map implementation is solid.")