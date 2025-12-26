# Aplikasi kasir sederhana

import os
import json

# Nama file database
nama_file_database = "data_pemutar_musik.json"

def baca_data():
    try:
        with open(nama_file_database, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def tambah_data(nama_lagu, penyanyi, durasi):
    data = baca_data()
    data.append({"nama_lagu": nama_lagu, "penyanyi": penyanyi, "durasi": durasi})
    with open(nama_file_database, 'w') as file:
        json.dump(data, file)
    print("Data berhasil ditambahkan!")

def hapus_data(nama_lagu):
    data = baca_data()
    data_baru = [lagu for lagu in data if lagu["nama_lagu"] != nama_lagu]
    with open(nama_file_database, 'w') as file:
        json.dump(data_baru, file)
    print("Data berhasil dihapus!")

def tampilkan_data():
    data = baca_data()
    if not data:
        print("Belum ada data.")
    else:
        print("Data Pemutar Musik:")
        for i, lagu in enumerate(data, 1):
            print(f"{i}. Nama Lagu: {lagu['nama_lagu']}, Penyanyi: {lagu['penyanyi']}, Durasi: {lagu['durasi']}")

def cari_data(keyword):
    data = baca_data()
    hasil_pencarian = [lagu for lagu in data if keyword.lower() in lagu["nama_lagu"].lower() or keyword.lower() in lagu["penyanyi"].lower()]
    if hasil_pencarian:
        print("Hasil Pencarian:")
        for lagu in hasil_pencarian:
            print(f"Nama Lagu: {lagu['nama_lagu']}, Penyanyi: {lagu['penyanyi']}, Durasi: {lagu['durasi']}")
    else:
        print("Tidak ada lagu yang sesuai dengan pencarian.")

def sorting_data():
    data = baca_data()
    data.sort(key=lambda x: x["nama_lagu"])
    with open(nama_file_database, 'w') as file:
        json.dump(data, file)
    print("Data berhasil diurutkan berdasarkan nama lagu.")

# Contoh Penggunaan
tambah_data("Perfect", "Ed Sheeran", "4:23")
tambah_data("Shape of You", "Ed Sheeran", "3:53")
tambah_data("Someone You Loved", "Lewis Capaldi", "3:02")
tampilkan_data()

cari_data("Ed Sheeran")

hapus_data("Perfect")
tampilkan_data()

sorting_data()
tampilkan_data()
