#Aplikasi Kasir Sederhana

# yang berhasil : file, function(sebagian), list,dict,dkk, string
# belum : masukin menu ke file menu_kasir, fungsi masukkin menu ke file, serta mencari riwayat file langsung dari program

#import
import datetime as dt

#fungsi 
def pembayaran(jumlah, harga_menu, diskon=0, pajak=0): 
    # Menghitung total biaya sebelum diskon
    for x in list_beli:
        total_biaya = float(jumlah * harga_menu)
    
    # Menghitung diskon
    diskon_amount = total_biaya * (diskon / 100)
    total_biaya_2 = total_biaya - diskon_amount
    
    # Menambah pajak
    pajak_amount = total_biaya * (pajak / 100)
    total_biaya_akhir = total_biaya + pajak_amount

    return total_biaya_akhir

def input_riwayat():
    time = dt.datetime.now()
    with open('riwayat_kasir.txt', 'a') as file:
        file.write('\n' + '-' * 17 + ' Bukti Transaksi Baru '.upper() + '-' * 16 + '\n')
        file.write('\n' + ' ' * 16 + time.strftime('%A, %d %B %Y') + '\n')    
        file.write('\n' + ' ' * 24 + time.strftime('%H:%M %p') + '\n')    
        file.write('\n' + ' ' * 10 + 'Menu yang dipesan: {}\n'.format(nama_menu)) 
        file.write('\n' + ' ' * 10 + 'Jumlah yang dipesan: {}\n'.format(jumlah))
        file.write('\n' + ' ' * 10 + 'Total biaya: {}\n'.format(bayar))
        file.write('\n' + '-' * 9 + ' Terimakasih Sudah Bertransaksi Di Sini '.upper() + '-' * 8 + '\n')
    with open('riwayat_kasir.txt', 'r') as file:
        print(file.read(), '\n')

#var
menu = {
    '1. Susu UHT 1L': 15000,
    '2. Keripik ': 10000,
    '3. Soda 250mL': 8000,
    '4. Popok Bayi': 50000,
}

# mulai algo

print('-' * 5, 'aplikasi kasir sederhana'.title(), '-' * 5)
print('Daftar Menu')

for i in menu:
    print(i, '\t : ', menu[i])

list_beli = {}

# mengakses menu menggunakan bilangan
while True:
    try:
        indeks = int(input('Masukkan nomor menu (1, 2, 3, dst.): ')) - 1  # Mengurangkan 1 karena indeks dimulai dari 0
        if indeks >= 0:
            keys = list(menu.keys())
            if indeks < len(keys):
                nama_menu = keys[indeks]
                harga_menu = menu[nama_menu]
                print(f'Menu: {nama_menu}, Harga: {harga_menu}')
                
                jumlah = int(input('Jumlah Pesanan : '))
                list_beli[nama_menu] = list_beli.get(nama_menu, 0) + jumlah

                print(list_beli)
                q = input('Apakah ada tambahan? y/n : ')
                if q.lower() != 'y':
                    break
    except ValueError:
        print('Menu tidak ditemukan. Harap masukkan yang benar')

# Perhitungan
bayar = pembayaran(jumlah, harga_menu, pajak = 10)

# menulis data ke file
input_riwayat()

print("Data transaksi baru berhasil ditambahkan ke dalam file 'riwayat_transaksi.txt'.")
exit()