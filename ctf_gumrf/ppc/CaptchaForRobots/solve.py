from pwn import *

from time import sleep
from base64 import b16decode, b32decode, b64decode, b85decode
import codecs

con = remote('46.254.20.217', 1336)
sleep(2)
con.recvuntil("GL&HF --------------")
while True:
    res = con.recv().decode().lstrip()
    if "4hsl33p" in res:
        print(res)
        break
    if len(res.split("\r\n")) > 2:
        task = res.split("\r\n")[1].split(" | ")
    else:
        task = res.split("\r\n")[0].split(" | ")
    print("Task:", task[0], task[1], task[2])
    if task[2] == "base85":
        ans = b85decode(task[1].encode()).decode()
        print('Sended b85:', ans)
        con.sendline(ans)
    elif task[2] == "base64":
        ans = b64decode(task[1].encode()).decode()
        print('Sended b64:', ans)
        con.sendline(ans)
    elif task[2] == "base32":
        ans = b32decode(task[1].encode()).decode()
        print('Sended b32:', ans)
        con.sendline(ans)
    elif task[2] == "base16":
        ans = b16decode(task[1].encode()).decode()
        print('Sended b16:', ans)
        con.sendline(ans)
    elif task[2] == "rot13":
        ans = codecs.decode(task[1], 'rot_13')
        print('Sended rot13:', ans)
        con.sendline(ans)
    print('-' * 20)
    sleep(0.1)