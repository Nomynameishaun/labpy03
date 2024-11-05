

# Meminta input jumlah bilangan acak
n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))

# Inisialisasi list untuk menyimpan bilangan acak
hasil = []

# Loop untuk menghasilkan bilangan acak
while len(hasil) < n:
    bilangan = random.random()
    if bilangan < 0.5:
        hasil.append(bilangan)

# Menampilkan hasil
for i, bilangan in enumerate(hasil, start=1):
    print(f"Bilangan ke-{i}: {bilangan}")