import threading

# Variables to store the results
add_result = None
multiply_result = None

# Function for the first thread (addition)
def add_thread():
    global add_result
    add_result = 1 + 2

# Function for the second thread (multiplication)
def multiply_thread():
    global multiply_result
    multiply_result = add_result * 2

# Create two threads
addition_thread = threading.Thread(target=add_thread)
multiplication_thread = threading.Thread(target=multiply_thread)

# Start both threads
addition_thread.start()
multiplication_thread.start()

# Wait for both threads to finish
addition_thread.join()
multiplication_thread.join()

# Print the final result
print("1 + 2 * 2 =", multiply_result)