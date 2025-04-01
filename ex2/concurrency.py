import threading
import time

class OrderedPrinter:
    def __init__(self):
        self.lock = threading.Lock()
        self.current_thread = 0
        self.total_threads = 5

    def print_message(self, message, thread_number):
        while True:
            with self.lock:
                if thread_number == self.current_thread:
                    print(message, end='')
                    self.current_thread += 1
                    break
            time.sleep(0.001)  # Small delay to prevent busy waiting

def concurrency_with_coffee():
    # Print initial message
    print("- I'm tired, Bob! ", end='')
    
    # Define messages in the correct order
    messages = [
        ("Do you know ", 0),          # Thread 2
        (" that our bodies ", 1),     # Thread 4
        ("are made of coffee? ", 2),  # Thread 1
        ("-Try drinking ", 3),        # Thread 5
        ("it! ", 4)                   # Thread 3
    ]
    
    printer = OrderedPrinter()
    threads = []
    
    # Create and start threads in order
    for message, thread_number in messages:
        thread = threading.Thread(target=printer.print_message, args=(message, thread_number))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Print final message
    print("- You're right!")

if __name__ == "__main__":
    concurrency_with_coffee()