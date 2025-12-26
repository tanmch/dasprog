print('bil.terbesar')

a= int(input('masukkan bilangan pertama : '))
b= int(input('masukkan bilangan kedua : '))
c= int(input('masukkan bilangan ketiga : '))
d= int(input('masukkan bilangan keempat: '))

bilangan_terkecil=a
bilangan_terbesar=d

if b < bilangan_terkecil:
   bilangan_terkecil=b
elif b > bilangan_terkecil:
   bilangan_terbesar=b
elif c < bilangan_terkecil:
   bilangan_terkecil=c
elif c > bilangan_terkecil:
   bilangan_terbesar=c
elif d < bilangan_terkecil:
   bilangan_terkecil=d
elif d > bilangan_terkecil:
   bilangan_terbesar=d
else:
   bilangan_terbesar=a


if a == b == c == d:
   print('4 Bilangan Sama Besar', bilangan_terbesar)
elif a == b == c:
   print('3 Bilangan Sama Besar', bilangan_terbesar)
elif a == b:
   print('2 Bilangan Sama Besar', bilangan_terbesar)
else : print(bilangan_terbesar)

