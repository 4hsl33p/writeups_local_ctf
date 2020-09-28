from pwn import *
from time import sleep

def get_spiral(m):
    return list(m[0]) + get_spiral(list(zip(*m[1:]))[::-1]) if m else []

def solver(matrix, mod):
    matrix_converted = get_spiral(matrix)
    res = 0
    for x in range(len(matrix_converted)-1):
        res += pow(matrix_converted[x], matrix_converted[x+1], mod)
    return str(res)

con = remote("46.254.20.217", 1337)
sleep(0.2)
con.recvuntil("---------------------------------").decode()

i = 0
while True:
    i+=1
    mod = int((con.recvuntil("Matrix:").decode()).split('\r\n')[-2])
    # print("Mod:", mod)
    matrix = (con.recvuntil(">>").decode()).split('\r\n')[1:-1]
    matrix = [[int(x) for x in row.split(' ')[:-1]] for row in matrix]
    # print(matrix)
    ans = solver(matrix, mod)
    print(str(i) + ".", ans)
    con.sendline(ans)
    if i == 300:
        sleep(0.2)
        flag = (con.recvall().decode()).split('\r\n')[-2]
        print(flag)
        exit(0)