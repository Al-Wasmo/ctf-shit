
wanted =  [33601,10760,62873,63911,39745,62471,65158,29652,39777,12164,20416,33945,18465,17245,13049,40799,]
flag = [0 for i in range(16)]


# brute force all chars
for T in range(0,16):
    tmp = flag.copy()


    # brute force all the numbers
    for K in range(0xffff):
        tmp[T] = K
        i1 = 42591
        i2 = (i1 * 27342) % 65537

        # what the game is doing
        for j in range(16):
            for i in range(16):
                i3 = i1
                i1 = (i2 * 31149) % 65537 
                i2 = (i3 * 17627) % 65537
            
                if i1 > 32766:
                    i1 =  round(i1 / 3)
                tmp[i] = (i1 * tmp[i] + i2) % 65537
            tmp = tmp[-1:] + tmp[:-1]
        if tmp[T] == wanted[T]:
            print(K)
            flag[T] = K
            break

print(flag)

for i in flag:
    print(bytes.fromhex(hex(i)[2:]))


# wwf{I4n_1s_s0_pr0ud_0f_y0u_648f}