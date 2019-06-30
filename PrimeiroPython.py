a = 'asdfghj'
#pega ultima posição da string

for i in a:
    a = a[-1:]
    if a == "j":
        print('Foi')
        print(a)
    else:
        print("Não foi")
        print(a)