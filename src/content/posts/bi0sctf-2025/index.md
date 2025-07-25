---
title: bi0sctf{india_ctf}
published: 2025-06-10
description: India top 1 team CTF
image: ./cover.png
tags: [Crypto]
category: CTF
draft: false
---

- This CTF is organized by india's top 1 team `bi0s`
- I think the challenges are quite hard to me.

---

# Veiled XOR

The challenge gives `p^reversed(q)` as a hint for a rsa challenge.
```python
from Crypto.Util.number import getPrime, bytes_to_long
n = (p := getPrime(1024)) * (q := getPrime(1024))
print(f"n : {n}\nc : {pow(bytes_to_long(flag), 65537, n)}\nVeil XOR: {p ^ int(bin(q)[2:][::-1], 2)}")
# n : ...
# c : ...
# Veil XOR: ...
```

## What we know
- We already knew that a similar challenge that is `p^q` can be solved by this forum:
[<-link-to-forum->](https://math.stackexchange.com/questions/2087588/integer-factorization-with-additional-knowledge-of-p-oplus-q)

- But what about `p^reversed(q)`?
- Luckily, we found a solved writeup that is exactly this challenge. Big thanks to KevinLiu.

## Solution Script
- note that we can increase `NBITS`
- @ creds to: [KevinLiu](https://maplebacon.org/2022/10/cryptoverse-2022/)

```py
n = 2565099383...
e = 65537
ct = 787441922...
# p xor (reverse q)
xor = 2684507369...
NBITS = 1024

# q = highQ || lowQ and p = highP || lowP, where all high/low have idx bits
def find(idx, lowP, highP, lowQ, highQ):

    if idx == NBITS:
        assert highP * highQ == n
        print("FOUND!")
        print(highP)
        print(highQ)
        exit()


    highX = (xor >> (NBITS - 1 -idx)) & 1
    lowX = (xor >> idx) & 1

    possibleLow = []
    possibleHigh = []
    
    # find possible (highP, lowQ) pairs from the MSB of the XOR
    if highX == 1:
        possibleHigh.append(((highP << 1) | 1, lowQ))
        possibleHigh.append((highP << 1, lowQ + (1 << idx)))
    else:
        possibleHigh.append((highP << 1, lowQ))
        possibleHigh.append(((highP << 1) | 1, lowQ + (1 << idx)))
    
    # find possible (lowP, highQ) pairs from the LSB of the XOR
    if lowX == 1:
        possibleLow.append((lowP, (highQ << 1) | 1))
        possibleLow.append((lowP + (1 << idx), highQ << 1))
    else:
        possibleLow.append((lowP, highQ << 1))
        possibleLow.append((lowP + (1 << idx), (highQ << 1) | 1))


    for highP, lowQ in possibleHigh:
        for lowP, highQ in possibleLow:
            # prune lower bits
            if lowP * lowQ % (1 << (idx + 1)) != n % (1 << (idx + 1)):
                continue
            
            pad = NBITS-1-idx

            # check upper bit bounds
            if (highP << pad) * (highQ << pad) > n:
                continue

            if ((highP << pad) + (1 << pad) - 1) * ((highQ << pad) + (1 << pad) - 1) < n:
                continue

            find(idx+1, lowP, highP, lowQ, highQ)

import sys
sys.setrecursionlimit(NBITS + 50) # set higher limit
find(0, 0, 0, 0, 0)
```

## To decrypt flag with p and q:
```python
from Crypto.Util.number import inverse, long_to_bytes
p =
q =
n =
c = 
phi = (p-1)*(q-1)
d = inverse(0x10001, (p-1)*(q-1))
flag = long_to_bytes(pow(c, d, n)).decode()
print(flag)
```

## 🚩 Flag
**`bi0sCTF{X0rcery_R3ve3rsing_1s_4n_4rt_2d3e3d}`**













