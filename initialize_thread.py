import threading

def broadcast_thread(thread_num):
    print(f"This is thread {thread_num}!")

threads = []

"""Create 4 threads""""
for i in range(4):
    """ Using thread class to execute a function """
    thread = threading.Thread(target=broadcast_thread, args = (i,))
    threads.append(thread)
    thread.start()

""" Wait for all threads to finish """"
for thread in threads:
    thread.join()

print("All threads are done: Proceed with main thread")

