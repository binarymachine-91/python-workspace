name1 = input('Enter First name: ')
name2 = input('Enter Second Name: ')
fla = 'FLAMES'
fla_mod = ''
com_lis = []
nam1_len = len(name1)
for alb in range(nam1_len):
    for alb2 in range(len(name2)):
        if name1[alb] == name2[alb2]:
            com_lis.append(name1[alb])
for com_alb in com_lis:
    name1 = name1.replace(com_alb,'')
    name2 = name2.replace(com_alb,'')
fin_len = len(name1) + len(name2)

while(len(fla) != 1):
    i,sls = divmod(fin_len,len(fla))
    if sls == 0:
        sls = len(fla) - 1
    else:
        sls = sls - 1
    fla_char = fla[sls]
    fla = fla.replace(fla_char,'')
    fla_mod = fla[sls:] + fla[:sls]
    fla = fla_mod
if fla == 'L':
    print("Your Releationship is 'LOVE'")
elif fla == 'F':
    print("Your Releationship is 'FRIEND'")
elif fla == 'A':
    print("Your Releationship is 'AFFECTION'")
elif fla == 'M':
    print("Your Releationship is 'MARRIAGE'")
elif fla == 'E':
    print("Your Releationship is 'ENEMY'")
elif fla == 'S':
    print("Your Releationship is 'SPOUSE'")
