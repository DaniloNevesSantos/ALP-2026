import time
import random

N = random.randint(2, 10)
time.sleep(N)
print("AGORA!")
T1 =time.time()
input()
T2 = time.time()
T3 = T2 - T1
print(f"Você demorou {T3}")