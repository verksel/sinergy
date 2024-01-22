print("Введите слово из латинских букв")
w = input()
c_a = 0
c_e = 0
c_i = 0
c_o = 0
c_u = 0
for i in range(len(w)):
    if w[i] == 'a':
        c_a += 1
    elif w[i] == 'e':
        c_e += 1
    elif w[i] == 'i':
        c_i += 1
    elif w[i] == 'o':
        c_o += 1
    elif w[i] == 'u':
        c_u += 1
if c_a != 0:
    print("букв a -", c_a, "штук")
else:
    print("вукв a - FALSE")
if c_e != 0:
    print("букв e -", c_e, "штук")
else:
    print("вукв e - FALSE")
if c_i != 0:
    print("букв i -", c_i, "штук")
else:
    print("вукв i - FALSE")
if c_o != 0:
    print("букв o -", c_o, "штук")
else:
    print("вукв o - FALSE")
if c_u != 0:
    print("букв u -", c_u, "штук")
else:
    print("вукв u - FALSE")
