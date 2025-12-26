"""
#membaca file databaru.txt dengan mode write
file = open('databaru.txt','w')
#menulis kalimat di file databaru.txt
file.write("Belajar nulis di file\n")
file.write("nulis di file dengan mode write\n")
file.close()
print("\n")

#membaca file databaru.txt dengan mode write
file = open('databaru.txt','w')
#menulis kalimat baru di file databaru.txt
file.write("Coba tulis lagi\n")
file.close()

print("\n")

import os
os.remove("databaru.txt")

print("\n")


with open("data.txt", "a") as file:
    file.write("gunakan with untuk menutup file secara otomatis")

print("\n")



with open("dataku.txt", "r") as file:
    print(file.read())

try:
    with open("dataku.txt", "r") as file:
        print(file.read())
except:
    print("File gak ada")


print("\n") 

"""

print('APLIKASI KASIR TOKO ALAT TULIS')

pensil = input('Pembelian pensil = ')
hapusan = input('Pembelian penghapus = ')
buku = input('Pembelian buku = ')
beli = str(int(pensil)*1000 + int(hapusan)*500 + int(buku)*2000)

print('Pembelian = Rp',beli)

data = open('penjualan.txt','r')
penjualan = data.read()
data.close()

total = penjualan + beli
print('Total penjualan = Rp',total)
data = open('penjualan.txt','w')
data.write(str(total))
data.close()