# TIME MODULE

from threading import local
import time

initial = time.time()
# print(initial)

k = 0
while k<45:
    print("hello")
    # time.sleep(1)
    k+=1
print(f"While loop ran in {time.time() - initial} seconds")


for i in range(45):
    print("hello")
print(f"For loop ran in {time.time() - initial} seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)