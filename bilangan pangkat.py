"""
# perpangkatan
bil = int(input('Masukkan Bilangan : '))
pangkat = int(input('Masukkan Pangkat : '))

def hitung_pangkat(bil, pangkat):
    if pangkat > 1: 
        return bil * hitung_pangkat(bil, pangkat - 1)

    return bil
hasil = hitung_pangkat(bil, pangkat)
print(f'Hasil = {hasil}')
# fibonacci
def fibonacci(f):
    if f <= 1:
        return f 
    else:
        return (fibonacci(f-1) + fibonacci(f-2))

f = int(input('Masukkan Bilangan Yang Akan DiFibonnaci : '))

print("Deret bilangan Fibonacci:")
for i in range(f):
    print(fibonacci(i), end=" ")

# Factorial 
def factorial(n):
    if n == 0:
        return 1
    if n >= 1:
        return n * factorial(n-1)

n = int(input("masukkan bilangan yang akan difaktorialkan : "))

hasil = factorial(n)
print(f'Hasil = {hasil}')

"""
# min max
def nilai_maksimal(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], nilai_maksimal(list[1:]))

def nilai_minimal(list):
    if len(list) == 1:
        return list[0]
    else:
        return min(list[0], nilai_minimal(list[1:]))

a = int(input('Masukkan Bilangan Pertama : ')) 
b = int(input('Masukkan Bilangan Kedua : ')) 
c = int(input('Masukkan Bilangan Ketiga : ')) 
d = int(input('Masukkan Bilangan Keempat : ')) 

lists = [a, b, c, d]

print(f"List: {lists}")
print(f"Nilai maksimal: {nilai_maksimal(lists)}")
print(f"Nilai minimal: {nilai_minimal(lists)}")
