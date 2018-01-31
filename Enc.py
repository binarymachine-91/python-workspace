inp_val = []
out_val = []
i = 0
in_chk = 0
op_chk = 0
fin_dec = 0
inp_val2 = 0
dec_loop = 0
#print('***************** Simple Encrpter and Decrypter Program **************')
#print('   $$$$$$$$$$$$$$$$$ Logic R.Sankar  Code : G.vignesh $$$$$$$$$       ')
#print('                 ~~~~~~~~ Verson 1.0 ~~~~~~~~                         ')
print('''
|..======================.|
||......Simple Encrypter and Decrypter..||
||......Logic : Mr.R.Sankar.............||
||......Code  : Mr.G.Vignesh............||
||......I .-------.OT T,......................||
||......./..><....\ .. ./.......................||
||......|.............| /\........................||
||.......\______/ /\/.........................||
||.........(____) / /...........................||
||.__/ _ . _. ___/________________||
|'.==\___\_).|==============.'|
︱︱︱.|____|
︱︱︱.| .|| .|
︱︱︱.|_||_|
︱︱︱(__)(__)
''')
while op_chk == 0:
    op = int(input('1.Encrypt 2.Decrypt 3.Exit\n'))
    if op > 3:
        print('Invalid Option')
        op_chk = 0
    else:
        op_chk = 1
#Encryption
if op == 1: #Condition Check
    print('Encryption Block')
    while in_chk == 0:
        n_inp = int(input('No of Inputs(1-32) : '))
        if n_inp > 32:
            print('Out of the range Input')
            in_chk = 0
        else:
            in_chk = 1

    # Loop for getting Input
    for i in range(n_inp):
        while inp_val2 == 0:
            inp_plc = i + 1
            val = input('Enter the Number {}: '.format(inp_plc))
            if int(val) > 255:
                print('Number Should be 0 to 255')
                inp_val2 = 0
            else:
                break
        inp_val.append(val)

    # Encryption Begins Here
    for j in range(len(inp_val)):
        if j == 0:
            decrp_val = int(inp_val[j]) * 256
            fin_dec = decrp_val + int(inp_val[j+1])
        elif j == len(inp_val) - 1:
            break
        else:
            decrp_val = int(fin_dec) * 256
            fin_dec = decrp_val + int(inp_val[j+1])
    print('Encrypted Value : {}'.format(fin_dec))
    ex = input('Press Enter to Exit')
# Decryption Block
elif op == 2:
    print('Decryption Block')
    cipher_txt = int(input('Enter the Encrypted Value : '))
    while dec_loop == 0:
        qut,rem = divmod(cipher_txt,256)
        out_val.append(rem)
        cipher_txt = qut
        if qut < 255:
            out_val.append(qut)
            dec_loop = 1
    out_val.reverse()
    print('Decrypted Input : {}'.format(out_val))
    ex = input('Press Enter to Exit')

# Exit from Program
elif op == 3:
    print('Thank You')
