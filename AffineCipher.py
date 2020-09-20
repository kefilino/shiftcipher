# Nama  : Kefilino Khalifa Filardi
# NPM   : 140810180028
# Tgl   : 2020.09.16
# Desc  : Program untuk enkripsi menggunakan Affine Cipher

def mod_inverse(a, m) :
    a = a % m
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def encrypt(x, a, b) :
    y = ''
    for i in x :
        if str.isalpha(i) or i == ' ' :
            if int(ord(i)) == 32 : 
                y = y + i
            else :
                if str.isupper(i) : 
                    i = int(ord(i) - 65)
                    i = (a * i + b) % 26
                    y = y + chr(i + 65)
                else :
                    i = int(ord(i) - 97)
                    i = (a * i + b) % 26
                    y = y + chr(i + 97)
    return y

def decrypt(y, a, b) :
    x = ''
    for i in y :
        if str.isalpha(i) or i == ' ' :
            if int(ord(i)) == 32 : 
                x = x + i
            else :
                if str.isupper(i) : 
                    i = int(ord(i) - 65)
                    i = mod_inverse(a, 26) * (i - b) % 26
                    x = x + chr(i + 65)
                else :
                    i = int(ord(i) - 97)
                    i = mod_inverse(a, 26) * (i - b) % 26
                    x = x + chr(i + 97)
    return x

x = input("Kalimat yang akan dienkripsi\t: ")

a = int(input("Masukkan nilai a\t\t: "))
b = int(input("Masukkan nilai b\t\t: "))
m = 26

y = encrypt(x, a, b)
x = decrypt(y, a, b)
print("\nPlaintext setelah dienkripsi\t: " + y)
print("Ciphertext setelah didekripsi\t: " + x)