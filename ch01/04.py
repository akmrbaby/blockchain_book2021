# 参考：https://github.com/blockchain-programming/book2021/blob/master/Chapter01.md
# 難易度を 2^240 として，難易度未満のハッシュ値を得るための入力値とそのハッシュ値を求める。
# 実験を100回繰り返して，ハッシュ値が得られるまでの平均時間と分散を求めてください
# 平均1秒でターゲット未満のハッシュ値が得られる難易度をできるだけ正確に求めてください。

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

pow, hash = hashcash(2**240)
print(pow, hash)
