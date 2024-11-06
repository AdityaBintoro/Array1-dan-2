angka=[]

# meminta input pengguna
for i in range(5):
    elemen=int(input(f"masukan angka ke-{i+1}: "))
    angka.append(elemen)

# mengurutkan angka dalam array
angka.sort()

# menampilkan array yang sudah dinurutkan
print(f"array yang sudah diurutkan: {angka}")
