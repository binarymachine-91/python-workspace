# coding=utf-8
inp_val = []
out_val = []
i = 0
in_chk = 0
op_chk = 0
enc_chk = 0
dec_chk = 0
fin_dec = 0
inp_val2 = 0
dec_loop = 0
ex = 0
import re
#print('***************** Simple Encrpter and Decrypter Program **************')
#print('   $$$$$$$$$$$$$$$$$ Logic R.Sankar  Code : G.vignesh $$$$$$$$$       ')
#print('                 ~~~~~~~~ Verson 1.0 ~~~~~~~~                         ')
print('''
|..======================.|
||......Simple Encrypter and Decrypter V2.0..||
||......Logic : Mr.R.Sankar................. ||
||......Code  : Mr.G.Vignesh.................||
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
    elif op == 1:
        #op_chk = 1
#Encryption Blok
        #in_chk = 0
        while enc_chk == 0:
            if op == 1: #Condition Check
                print('Encryption Block')
                while in_chk == 0:
                    try:
                        n_inp = int(input('No of Inputs(1-32) : '))
                        if n_inp > 32:
                            print('Out of the range Input')
                            in_chk = 0
                    except ValueError:
                        print('Input must be a number')
                    else:
                        in_chk = 1

                # Loop for getting Input
                inp_val.clear()
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
                #def encrypt_no(inp_val):
                # Encryption Begins Here
                fin_dec = 0
                for j in range(len(inp_val)):
                    if j == 0:
                        encry_val = int(inp_val[j]) * 256
                        fin_dec = encry_val + int(inp_val[j + 1])
                    elif j == len(inp_val) - 1:
                        break
                    else:
                        encry_val = int(fin_dec) * 256
                        fin_dec = encry_val + int(inp_val[j + 1])
                fin_dec_str = str(fin_dec)
                n_inp_str = str(n_inp * 2)
                n_inp_str = n_inp_str.zfill(2)
                dec_val = fin_dec_str + n_inp_str
                print('Encrypted 1Value : {}'.format(dec_val))
                ex = int(input('Press 1.Back 2.Continue Encryption\n'))
                if ex == 1:
                    enc_chk = 0
                    in_chk = 0
                    break
                elif ex == 2:
                    enc_chk = 0
                    in_chk = 0

# Decryption Block
    elif op == 2:
        while dec_chk == 0:
            print('Decryption Block')
            cipher_txt = int(input('Enter the Encrypted Value : '))
            cipher_txt_str = str(cipher_txt)
            cipher_txt = int(cipher_txt_str[:-2])
            n_inp_dec = cipher_txt_str[-2:]
            n_inp_dec_in = int(n_inp_dec)/2
            dec_loop = 0
            out_val.clear()
            #Decrption Begins here
            while dec_loop == 0:
                qut,rem = divmod(cipher_txt,256)
                out_val.append(rem)
                cipher_txt = qut
                if qut < 255:
                    out_val.append(qut)
                    dec_loop = 1
            out_val.reverse()
            zero_cnt = n_inp_dec_in - len(out_val)
            for k in range(int(zero_cnt)):
                out_val.insert(0,0)
            print('Decrypted Input : {}'.format(out_val))
            ex = int(input('1.Back 2.Continue Decrypt\n'))
            if ex == 2:
                dec_chk == 0
            else:
                op_chk = 0
                break
    else:
        print('Thank You')
        op_chk = 1
