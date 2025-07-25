---
title: SKR{gr1nd1ng_f14gs}
published: 2025-01-03
image: ./cover.png
tags: [Crypto]
category: CTF
draft: false
---

My grind for crypto and web challenges.

---

## Small-E_2-Writeup

Description

1. Type: #cryptography #rsa
2. Desc: Damn! Someone decrypted my flag! Nevermind, I have upgraded my python script, now no one can decrypt my flag hehe..
3. Vuln:
   - small `e`
   - no padding
4. Attacks:
   - small `e` attack
5. File:
   `chall.py`

---

### How to solve?

Here's my script to solve this:

```python
import gmpy2
from libnum import n2s

n = 91916062929755899991419452098776070211257414596875218275380603377591870182603435387592799597601677412725463330022618304491967226095274532701595395513081487786880774375261242719962843053332094817389705801521607097644046054957895718424075514672164946208067840011762933432075645942010887315772486354077753098921
c = 35783243553484273090677089927059990920007599084499143586613182895028518498096602289698991044152216674632952484103049422671044257404009588038522559515118720479025871564218557941067601815602070912535220611164761904849438827907551620715608094645194620571566118891025017218047159723272277310954299826359459603893
e = 5

for k in range(1, 100000):
    m, exact = gmpy2.iroot(c + k*n , e)
    if pow(m, e, n) == c:
        print("Flag: ", n2s(int(m)))
        break
```

\*note: I use `n2s` for conversion from integers into ASCII string.

### Explanation?

Given `n, e, c` and we know that `e = 5` is small.

We know that:
$$ c \equiv m^e \pmod{n}$$
and `modular arithmetic`, `c` is the remainder of `m^e / n` :

$$c = m^e-kn$$

subject m, we get:
$$m = \sqrt[e]{c + kn}$$

Since
$$m^e ≥ n$$
we can brute force `k` since `e` is small value.

Check back the value:

```python
    if pow(m, e, n) == c:
```

Voila~
Flag: ||SKR{17_St1ll_t00_5m411}||

---
