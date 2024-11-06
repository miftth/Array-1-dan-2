matriks = []

print("masukan elemen matriks 3x3:")
for i in range(3):
    baris=[]
    for j in range(3):
        nilai= int(input(f"Masukan Elemen Baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks.append(baris)


    transpose = []
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks[j][i])
        transpose.append(baris)

print("\nHasil Transpose Matriks : ")
for baris in transpose:
    print(baris)