import threading
import time

def target(second):
    print(f'Treading {threading.current_thread().name} is running')
    print(f'Treading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Treading {threading.current_thread().name} is ended')

print(f'Treading {threading.current_thread().name} is running')

threads = []
for i in [1, 5]:
    thread = threading.Thread(target=target, args=[i])
    threads.append(thread)  # append sub thread
    thread.start()

for thread in threads:
    thread.join()

print(f'Treading {threading.current_thread().name} is ended')