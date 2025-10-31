class Node:
    def __init__(self,key,value):
        self.key = key
        self.value =value
        self.next = None

class HashMap:
    def __init__(self,capacity=10):
        self.capacity = capacity
        self.array = [None] * self.capacity

    def _hash(self,key):
        return abs(hash(key)) % self.capacity
    
    def put(self,key,value):
        index = self._hash(key)
        current_node = self.array[index]

        if current_node is None:
            self.array[index] = Node(key,value)
            return
        
        prev_node = None
        while current_node is not None:
            if current_node.key == key:
                current_node.value = value
                return
            
            prev_node = current_node
            current_node = current_node.next
        
        prev_node.next = Node(key,value)


    def get(self,key):
        index = self._hash(key)
        current_node = self.array[index]

        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next

        raise KeyError(f"Key {key} not found")
    
def print_all_count(hash_map):
    print("--- All IP Addressess ---")
    found_item = False

    for i in range(hash_map.capacity):
        current_node = hash_map.array[i]
        while current_node is not None:
            print(f"IP Address: {current_node.key}, Count: {current_node.value}")
            found_item = True
            current_node = current_node.next

    if not found_item:
        print("No IP addresses found.")

    
def analyze_logs(file_name):
    ip_count = HashMap(capacity=20)
    print(f"Opening log file: {file_name} ...")
    lines_processed = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                ip_address = line.split(' ')[0]
                try:
                    current_count = ip_count.get(ip_address)
                    ip_count.put(ip_address,current_count +1)
                except KeyError:
                    ip_count.put(ip_address,1)

                lines_processed +=1

        print(f"\n--- Log Analysis Complete ---")
        print(f"Total lines processed: {lines_processed}")
        return ip_count

    except FileNotFoundError:
        print(f"Error: Log file '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file_name = "access.log"
    final_counts = analyze_logs(file_name)

    if final_counts:
        print_all_count(final_counts)
