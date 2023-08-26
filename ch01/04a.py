# 平均時間と分散
import time
import hashlib
import random

def hashcash(target):
    pow = ""
    size = 2 ** 256
    hash = 2 ** 256 + 1
    count = 0
    while hash >= target:
        pow = str(random.randint(0, size))
        hash = int(hashlib.sha256(pow.encode("utf-8")).hexdigest(), 16)
        count += 1
    return [pow, hash]


def hashcashTime(target):
    start = time.time()
    hashcash(target)
    end = time.time()
    return end - start

N = 100
TARGET = 2**240
time_list = []
for i in range(N):
    time_list.append(hashcashTime(2**240))
ave = time_list.mean()
print(ave)
