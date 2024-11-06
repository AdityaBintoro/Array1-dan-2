# deklarasi matrix
matriks=[]

# meminta input pengguna mengisi matrix 3x3
print("masukan elemen kedalam metrix 3x3:")
for i in range(3):
    baris=[]
    for j in range(3):
        nilai = int(input(f"masukan elemen baris {i+1}, kolom {j+1}:"))
        baris.append(nilai)
    matriks.append(baris)

# transpose matrix
transpose=[]
for i in range(3):
    baris=[]
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)

#menampilkan hasil matrix
print("\nhasil transpose matriks:" )
for baris in transpose:
    print(baris)