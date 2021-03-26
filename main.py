def hex2bin(hexInput):
    return str("{0:064b}".format(int(hexInput, 16)))
    
def int2bin(input):
    return str("{0:04b}".format(int(input)))
    
def bin2hex(binstr): 
    return str("{0:016X}".format(int(binstr, 2)))

mHex = "0 1 2 3 4 5 6 7 8 9 A B C D E F".replace(" ","")

xxxx = str("{0:07d}".format(int(str(input("Nhap MSSV: ")).replace(" ",""))))
keyHex = "0 1 2 3 4 5 6 7 8 9 A B".replace(" ","") + xxxx[-4:]
print("M: ", mHex)
print("Key: ", keyHex)

mBin = hex2bin(mHex)
keyBin = hex2bin(keyHex)

pc1Table = """57 49 41 33 25 17 9
1 58 50 42 34 26 18
10 2 59 51 43 35 27
19 11 3 60 52 44 36
63 55 47 39 31 23 15
7 62 54 46 38 30 22
14 6 61 53 45 37 29
21 13 5 28 20 12 4""".replace("\n"," ").split(" ")

pc2Table = """14 17 11 24 1 5
3 28 15 6 21 10
23 19 12 4 26 8
16 7 27 20 13 2
41 52 31 37 47 55
30 40 51 45 33 48
44 49 39 56 34 53
46 42 50 36 29 32""".replace("\n"," ").split(" ")

ipTable = """58 50 42 34 26 18 10 2
60 52 44 36 28 20 12 4
62 54 46 38 30 22 14 6
64 56 48 40 32 24 16 8
57 49 41 33 25 17 9 1
59 51 43 35 27 19 11 3
61 53 45 37 29 21 13 5
63 55 47 39 31 23 15 7""".replace("\n"," ").split(" ")

ip_1Table = """40 8 48 16 56 24 64 32
39 7 47 15 55 23 63 31
38 6 46 14 54 22 62 30
37 5 45 13 53 21 61 29
36 4 44 12 52 20 60 28
35 3 43 11 51 19 59 27
34 2 42 10 50 18 58 26
33 1 41 9 49 17 57 25""".replace("\n"," ").split(" ")

eTable = """32 1 2 3 4 5
4 5 6 7 8 9
8 9 10 11 12 13
12 13 14 15 16 17
16 17 18 19 20 21
20 21 22 23 24 25
24 25 26 27 28 29
28 29 30 31 32 1""".replace("\n"," ").split(" ")

pTable = """16 7 20 21
29 12 28 17
1 15 23 26
5 18 31 10
2 8 24 14
32 27 3 9
19 13 30 6
22 11 4 25""".replace("\n"," ").split(" ")

s1Table = """14 4 13 1 2 15 11 8 3 10 6 12 5 9 0 7
0 15 7 4 14 2 13 1 10 6 12 11 9 5 3 8
4 1 14 8 13 6 2 11 15 12 9 7 3 10 5 0
15 12 8 2 4 9 1 7 5 11 3 14 10 0 6 13""".split("\n")
s1Table = [temp.split(" ") for temp in s1Table]

kPlus = ''.join(keyBin[int(x)-1] for x in pc1Table)

c0 = kPlus[:28]
d0 = kPlus[28:]
c1 = c0[1:] + c0[0]
d1 = d0[1:] + d0[0]
c1d1 = c1 + d1

k1 = ''.join(c1d1[int(x)-1] for x in pc2Table)
print("K1: ", k1)

ip = ''.join(mBin[int(x)-1] for x in ipTable)

l0 = ip[:32]
r0 = ip[32:]
print("L0: ", l0)
print("R0: ", r0)

e_r0 = ''.join(r0[int(x)-1] for x in eTable)
print("E(R0): ", e_r0)

a = ''.join('0' if i == j else '1' for i, j in zip(k1,e_r0))
print("A: ", a)

b = []
for i in range(8):
    b.append(''.join(x for x in a[i*6:i*6+6]))
s = ''.join(int2bin(s1Table[int(x[0]+x[-1],2)][int(x[1:-1],2)]) for x in b)
print("S: ", s)

f = ''.join(s[int(x)-1] for x in pTable)
print("f: ", f)

r1 = ''.join('0' if i == j else '1' for i, j in zip(l0,f))
print("R1: ", r1)

l1 = r0
r1l1 = r1 + l0
ip_1 = ''.join(r1l1[int(x)-1] for x in ip_1Table)
print("IP-1: ", ip_1)
print("Ciphertext: ", bin2hex(ip_1))