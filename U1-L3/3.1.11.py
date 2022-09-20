import time

i = 0
print("[", end="")
while i < 30:
    print("*", end="")
    time.sleep(0.1)
    i += 1
print("]")

