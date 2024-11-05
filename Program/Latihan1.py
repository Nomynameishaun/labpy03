import random
n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))
hasil = []
while len(hasil) < n:
    bilangan = random.random()
    if bilangan < 0.5:
        hasil.append(bilangan)
for i, bilangan in enumerate(hasil, start=1):
    print(f"Bilangan ke-{i}: {bilangan}")