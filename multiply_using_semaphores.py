import threading

# Shared result
result = 1

# Semaphore to control access to the shared result
semaphore = threading.Semaphore(1)

# Function for the threads (multiply by 2)
def double():
    global result
    while result < 2048:
        # Acquire the semaphore
        semaphore.acquire()
        if result < 2048:
            result *= 2
        # Release the semaphore
        semaphore.release()

# Create four threads for multiplying
threads = [threading.Thread(target=double) for _ in range(4)]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the final result
print("Final result:", result)