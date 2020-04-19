import threading
import time

class MyThread(threading.Thread):
    def __init__(self, second):
        threading.Thread.__init__(self)
        self.second = second

    def run(self):
        print(f'Treading {threading.current_thread().name} is running')
        print(f'Treading {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Treading {threading.current_thread().name} is ended')

print(f'Treading {threading.current_thread().name} is running')
threads = []

for i in [1, 5]:
    thread = MyThread(i)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Treading {threading.current_thread().name} is ended')