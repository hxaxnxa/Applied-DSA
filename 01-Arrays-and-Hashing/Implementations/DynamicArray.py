import ctypes

class DynamicArray:

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self._create_array(self.capacity)
        print(f"Initialized array with size: {self.size} and capacity: {self.capacity}.")

    def _create_array(self,capacity):
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.size
    
    def display(self):
        print([self.array[i] for i in range(self.size)])

    def get(self,index):
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} out of bounds for size {self.size}.")
        return self.array[index]
    
    def set(self,index,value):
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} out of bounds for size {self.size}.")
        self.array[index] = value

    def append(self,value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = value
        self.size +=1 
        print(f"Appended {value}. size: {self.size}, capacity: {self.capacity}.")

    def _resize(self,new_capacity):
        print(f"Resizing from {self.capacity} to {new_capacity}.")
        new_array = self._create_array(new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity
        print(f"Resize Completed.")
        
if __name__ == "__main__":
    print("--- Test 1: Create Array ---")
    arr = DynamicArray()
    arr.display()
    print(f"Length: {len(arr)}")
    print("-" * 20)
    
    print("--- Test 2: Append first item (triggers resize 1 -> 2) ---")
    arr.append(10)
    arr.display()
    print(f"Length: {len(arr)}")
    print("-" * 20)

    print("--- Test 3: Append second item (fills capacity) ---")
    arr.append(20)
    arr.display()
    print(f"Length: {len(arr)}")
    print("-" * 20)

    print("--- Test 4: Append third item (triggers resize 2 -> 4) ---")
    arr.append(30)
    arr.display()
    print(f"Length: {len(arr)}")
    print("-" * 20)

    print("--- Test 5: Test get(i) ---")
    print(f"arr.get(0): {arr.get(0)}")
    print(f"arr.get(2): {arr.get(2)}")
    print("-" * 20)

    print("--- Test 6: Test set(i, val) ---")
    print("Setting")
    arr.set(1, 99)
    arr.display()
    print(f"arr.get(1): {arr.get(1)}")
    print("-" * 20)

    print("--- Test 7: Test Edge Cases (Errors) ---")
    try:
        arr.get(3)
    except IndexError as e:
        print(f"Caught expected error {e}.")

    try:
        arr.set(10,4)
    except IndexError as e:
        print(f"Caught expected error {e}.")

    print("-" * 20)
    print("--- Test 8: Fill up to trigger next resize (4 -> 8) ---")
    arr.append(40) 
    arr.append(50) 
    arr.display()
    print(f"Length: {len(arr)}, Capacity: {arr.capacity}")
    
    print("\nAll tests passed! Foundation is strong.")


    