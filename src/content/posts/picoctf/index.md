---
title: picoctf
published: 2024-09-09
description: "Intro to CTFs"
image: ./cover.png
tags: [Linux, Forensics]
category: CTF
draft: false
---

# Serpentine

This is the most challenging question Ive solved (took me 6hrs), the logic is to open flag.txt or even run bash command without even typing the **letters**!

<img width="228" alt="img1" src="https://github.com/user-attachments/assets/c7f6aa4f-fea7-4f46-b34c-11e0b1a9fdd6" />

So, after `*` I can tell there's a folder called blargh.

<img width="290" alt="img2" src="https://github.com/user-attachments/assets/3a251fbf-de33-404c-b969-e6288e17646b" />

when run `*/*`, it reveals a flag.txt inside blargh folder

<img width="302" alt="img3" src="https://github.com/user-attachments/assets/d2eb4476-7e8b-4549-b042-8c55ef2c3d4d" />

This is the secret: `special bash variable $_`
This can be used to see the last argument given to the previous command.

I asked my friend on more tips to solve this, and my friend gimme this link: [Can Bash substring offset be omiited?](https://stackoverflow.com/questions/75370113/can-bash-substring-offset-be-omitted)

Finally with the help of the letters `c, a, t` from on-calastran.txt, i can finally read the flag.txt file :D

<img width="566" alt="img4" src="https://github.com/user-attachments/assets/ff3f3812-3ca5-4f5a-b3aa-de881d27ecc2" />

---

# Scan Surprise
<img width="566" alt="scan" src="https://github.com/Exberg/ctf-writeups/blob/main/images/image1.png?raw=true"/>

this was the easiest thing ive done, just unzip files, open image and scan qr code.

---

# Verify
Author: Jeffery John
Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

<img width="576" alt="img5" src="https://github.com/user-attachments/assets/00fca880-5602-4e9a-b59b-54b3d509d098" />

first thing first, open linux and run the script. 

<img width="1059" alt="img6" src="https://github.com/user-attachments/assets/22ef7d42-ba78-43f4-b9a2-487d2eaeb6ca" />

After ls the files, i figured i can just loop them instead of checking one by one since its so tedious to do so.

---

# information
![cat](https://github.com/user-attachments/assets/70e6f365-eddd-4619-8da2-a2b0806d413c)

This is prob the hardest ive done, because when i actually looked at the hint.
Spoilers Alert: "look at the file" NOT THE CAT!

<img width="983" alt="img7" src="https://github.com/user-attachments/assets/249dc373-451f-4182-a5d4-ae66f6ddc9f9" />

So, i used exiftool to extract some juicy infos. At the beginning, i was like where's the answer??? But when i take a deep look, and i paste everything into the cyberchef, i found this particular line (highlighted in green) delivered me straight to the answer :P

---

# what's a net cat?
`
Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 64287 to get the flag?
`

I find this interesting because of the title lol

First, install netcat on terminal. Then, Connect to the Host and Port: nc jupiter.challenges.picoctf.org 64287

<img width="347" alt="img8" src="https://github.com/user-attachments/assets/67c31a19-66de-46fc-90c4-0e97a9393968" />

**so ezzZ = =**

# Serpentine - Find the flag in the Python script!
<img width="876" alt="img9" src="https://github.com/user-attachments/assets/aa2f2c8a-fa56-489e-bfdb-8b60305ce4fc" />

This one is pretty easy, just call this function `print_flag()`


