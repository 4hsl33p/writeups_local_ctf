data = "=:869=8m====9>9l96=>9<;h==8k8=9<979>=9=>9<;h9==>;h==9o9j"

for a in range(1,10):
    key = []
    key.append(57 ^ a ^ 99 ^ 53)
    b =  a + 8
    key.append(69 ^ b ^ 37 ^ 10)
    c = a * b
    key.append(51 ^ c ^ 30 ^ 40)
    d = c - 50
    key.append(36 ^ d ^ 80 ^ 47)
    e = 34 + a + b + d - c
    key.append(42 ^ e ^ 67)
    key.append(82 ^ key[0] ^ key[1])
    if e > 1:
        temp = pow(pow(a,e), pow(e, a), 777) ^ 8
        key.append(temp)
        key.append(1392 ^ key[3] ^ key[1] ^ 1337)
        key.append(73 ^ key[7] ^ key[6] ^ key[5] ^ key[4] ^ key[3] ^ key[2] ^ key[1] ^ key[0])
        [print(chr(x), end='') for x in key]
        # [print(x, end=' ') for x in key]
        print("\n")