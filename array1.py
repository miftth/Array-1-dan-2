angka = []

#meminta input pengguna
for i in range(5):
    elemen = int(input(f"Masukan Angka Ke-{i+1}: "))
    angka.append(elemen)

    #mengurutkan angka dalam array
    angka.sort()

    #Menampilkan array yang sudah di urutkan
print(f"array yang sudah di urutkan : {angka}")