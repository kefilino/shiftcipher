# Nama  : Kefilino Khalifa Filardi
# NPM   : 140810180028
# Tgl   : 2020.09.20
# Desc  : Program untuk enkripsi menggunakan Shift Cipher

def encrypt(x, k) :
    y = ''
    for i in x :
        if str.isalpha(i) or i == ' ' :
            if int(ord(i)) == 32 : 
                y = y + i
            else :
                if str.isupper(i) : 
                    i = int(ord(i) - 65)
                    i = (i + k) % 26
                    y = y + chr(i + 65)
                else :
                    i = int(ord(i) - 97)
                    i = (i + k) % 26
                    y = y + chr(i + 97)
    return y

def decrypt(y, k) :
    x = ''
    for i in y :
        if str.isalpha(i) or i == ' ' :
            if int(ord(i)) == 32 : 
                x = x + i
            else :
                if str.isupper(i) : 
                    i = int(ord(i) - 65)
                    i = (i - k) % 26
                    x = x + chr(i + 65)
                else :
                    i = int(ord(i) - 97)
                    i = (i - k) % 26
                    x = x + chr(i + 97)
    return x

x = input("Kalimat yang akan dienkripsi\t: ")

k = int(input("Masukkan nilai kunci K\t\t: "))
m = 26

y = encrypt(x, k)
x = decrypt(y, k)
print("\nPlaintext setelah dienkripsi\t: " + y)
print("Ciphertext setelah didekripsi\t: " + x)