# labpy03
Halo!, ini dibuat untuk memenuhi tugas yang diberikan
## Latihan 1
### Program Bilangan Acak Sederhana
```ruby
import random

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
```
Apabila dijalankan maka akan seperti berikut:
![1](<Gambar/randomb.png>)
### Flowchart

![1](<Gambar/randomf.png>)

## Latihan 2
### Program Investasi Perbulan Sederhana
```ruby
# Modal awal
modal_awal = 100_000_000  # 100 juta dalam rupiah

# Keuntungan per bulan
keuntungan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.02]

# Menghitung total keuntungan
total_keuntungan = 0

# Loop untuk menghitung keuntungan tiap bulan
for bulan, persen_keuntungan in enumerate(keuntungan, start=1):
    laba_bulan = modal_awal * persen_keuntungan
    total_keuntungan += laba_bulan
    print(f"Bulan ke-{bulan}: Keuntungan = Rp {laba_bulan:,.0f}")

# Menampilkan total keuntungan selama 8 bulan
print(f"\nTotal keuntungan selama 8 bulan = Rp {total_keuntungan:,.0f}")
```
Apabila dijalankan maka akan seperti berikut:
![1](<Gambar/Modalk.png>)
### Flowchart

![1](<Gambar/Modalf.png>)
