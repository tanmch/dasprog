"""
nama = 'Wahid Abdulloh'
asal = "Indonesia"

print("\n")

print('Dia berkata: "Pergilah!"')

# menggunakan petik satu
print('Aku menimpali: "Apakah kau ingin aku \'angkat kaki\'?!"')
# menggunakan petik dua
print("Aku menimpali: \"Apakah kau ingin aku 'angkat kaki'?!\"")


print("\n")
print('\\(^^ \) (/ --/)')
print("\n")

berita = 'Ramai-ramai developer di seluruh dunia mulai menggunakan \
teks editor masa kini seperti Visual Studio Code, \
atom, sublime text, dan lain sebagainya.'
print('sublime text' in berita) # output: True
print('notepad++' in berita) # output: False

print("\n")

nama = 'Lendis Fabri'
print(nama[4]) # output: i
print(nama[7]) # output: F
print(nama[-1]) # output: i
print(nama[-3]) # output: b

print("\n")

judul = 'Pelajaran Matematika Untuk SD'
print(judul[0:5]) # output: Pelaj
print(judul[:10]) # output: Pelajaran
print(judul[10:15]) # output: Matem
print(judul[-1:-3]) # output:
print(judul[:-3]) # output: Pelajaran Matematika Untuk
print(judul[-5:]) # output: uk SD

print("\n")

print(len('Indonesia')) # output: 9
print(len('Malaysia')) # output: 8

print("\n")

nomor_telepon_1 = '0871122334455'
nomor_telepon_2 = '6288776655300'
nomor_telepon_3 = '+6233003300330'
kode_negara = '+62'
print(nomor_telepon_1.startswith(kode_negara)) # False
print(nomor_telepon_2.startswith(kode_negara)) # False
print(nomor_telepon_3.startswith(kode_negara)) # True

print("\n")

email_1 = 'presiden@gmail.com'
email_2 = 'presiden@outlook.com'
print(email_1.endswith('gmail.com')) # True
print(email_2.endswith('gmail.com')) # False

nama_depan = 'Renza'
nama_belakang = 'Ilhami'
nama_lengkap = nama_depan + nama_belakang
print(nama_lengkap)
nama_lengkap = nama_depan + ' ' + nama_belakang
print(nama_lengkap) # output: Renza Ilhami

print("\n")

print('Sekarang tahun: ' + str(2021))

print("\n")

print('----------') # output: ----------
print('-' * 10) # ouput: ----------

template = 'Halo, saya %s dari %s'
print(template % ('Lendis Fabri', 'Indonesia'))
# output: Halo, saya Lendis Fabri dari Indonesia

print("\n")

template = 'Halo, saya {nama} dari {asal}'
template_2 = 'Saya suka makan {} dan minum {}'
print(template.format(nama = 'Lendis Fabri', asal = 'Indonesia'))
# Halo, saya Lendis Fabri dari Indonesia
print(template_2.format('Nasi Goreng', 'air putih'))
# Saya suka makan Nasi Goreng dan minum air putih

print("\n")

nama = 'Lendis Fabri'
asal = 'Indonesia'
print(f'Perkenalkan saya {nama} dari {asal} 😎')


alamat = 'Surabaya, Jawa Timur, Indonesia'
print(alamat.split())
# ['Surabaya,', 'Jawa', 'Timur,', 'Indonesia']
print(alamat.split(','))
# ['Surabaya', ' Jawa Timur', ' Indonesia']
print(alamat.split(', '))
# ['Surabaya', 'Jawa Timur', 'Indonesia']
print('❤️'.join(['aku', 'suka', 'python']))
# aku❤️suka❤️python
print('🦖'.join(alamat.split(', ')))
# Surabaya🦖Jawa Timur🦖Indonesia
print("\n")

print('halo selamat pagi!'.upper())
print('Halo Selamat Siang!'.upper())

print("\n")

print('APA KABAR?'.lower())
print('Lagi Dimana?'.lower())


print('daun tidak pernah membenci angin'.title())
print('LASKAR PELANGI'.title())

print("\n")

print('Indonesia Adalah Negara Kepulauan'.swapcase())
print('aKu cInTa NeGeRiKu'.swapcase())

print("\n")

angka = '12345'
print('Index angka 3:', angka.find('3'))
print('Index angka 45:', angka.find('45'))
print('Index angka 35:', angka.find('35'))

print("\n")

ibu_kota = 'Jakarta'
print(ibu_kota.replace('a', 'i'))
print(ibu_kota.replace('kar', 'X'))


ibu_kota = 'Jakarta'
print(ibu_kota.replace('a', ''))

print("\n")

"""
paragraf = 'Baru-baru ini telah ditemukan sebuah meteor di suatu sungai'
x = paragraf.count('di')
print(f'Kata "di" muncul sebanyak {x} kali')

"""
print("\n")
"""