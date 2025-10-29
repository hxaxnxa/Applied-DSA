import ctypes

class DynamicArray:
    def __init__(self):
        self.size=0
        self.capacity=1
        self.array = self._create_array(self.capacity)
        print(f"Initialized array with size: {self.size} and capacity: {self.capacity}.")

    def _create_array(self,capacity):
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.size
    
    def get(self,index):
        if not 0<= index < self.size:
            raise IndexError(f"Index {index} out of bounds for size {self.size}.")
        return self.array[index]
    
    def append(self,value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = value
        self.size += 1
        print(f"Appended {value}. size: {self.size}, capacity: {self.capacity}.")

    def _resize(self,new_capacity):
        new_array = self._create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity =new_capacity

    def display(self):
        print([self.array[i] for i in range(self.size)])

def analyze_logs(log_file):
    ip_list = DynamicArray()
    print(f"Opening log file: {log_file} ...")
    try:
        with open(log_file,'r') as file:
            for line in file:
                if line.strip():
                    ip_address = line.split(' ')[0]
                    ip_list.append(ip_address)

        print(f"\n--- Log Analysis Complete ---")
        ip_list.display()
        return ip_list
    
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    log_file_name = "access.log"
    all_ips = analyze_logs(log_file_name)

    if all_ips:
        print(f"Total length : {len(all_ips)}")    
