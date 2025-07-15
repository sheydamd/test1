import threading
import time


def countdown(name, start):
    while start > 0:
        print(f"{name} → {start}")
        time.sleep(1)
        start -= 1
    print(f"{name} finished!")

t1 = threading.Thread(target=countdown, args=("Thread A", 5))
t2 = threading.Thread(target=countdown, args=("Thread B", 3))
t3 = threading.Thread(target=countdown, args=("Thread C", 7))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("✅ All threads completed.")