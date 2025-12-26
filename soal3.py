print('nilai dan usia')

# input 2 var. satu nilai, satu usia.
# jika nilainya >= 80 dan umur >= 20, outputnya selamat ya kak, kamu lulus
# jika nilai <= 80, maaf ya kak, coba lagi
# jika umur <= 20 dan nilai >= 80, outputnya selamat ya dek, kamu lulus.
# jika nilai <= 80 dan umur <= 20, maaf ya dek coba lagi
# output pesannya bebas        

a = int(input('Masukkan Nilai : '))
b = int(input('Masukkan Usia : '))

if a >= 80 and b >= 20 :
    print('Selamat Ya Kak, Kamu Lulus!')
elif a < 80 and b >= 20 :
    print('Maaf Ya Kak, Coba Lagi')
elif a < 80 and b < 20 :
    print('Maaf Ya Dek, Coba Lagi')
else: print('Selamat Ya Dek, Kamu Lulus')