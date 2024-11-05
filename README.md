# labpy03
Halo!, ini dibuat untuk memenuhi tugas yang diberikan
## Latihan 1
### Program Bahasa Python Bilangan Acak Sederhana
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
### Program Bahasa Python Investasi Perbulan Sederhana
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

## Latihan 3
### Program bahasa Python ATM Sederhana
```ruby
# Saldo awal pengguna
saldo = 1000000

# Fungsi untuk menampilkan menu dan melakukan penarikan
def atm():
    global saldo
    while True:
        print(f"\nSaldo saat ini: Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == '1':
            try:
                jumlah = int(input("Masukkan jumlah penarikan: "))
                if jumlah <= saldo:
                    saldo -= jumlah
                    print("Penarikan berhasil!")
                else:
                    print("Saldo tidak mencukupi!")
            except ValueError:
                print("Jumlah yang Anda masukkan tidak valid.")
        
        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu 1 atau 2.")
atm()
```
Apabila dijalankan maka hasilnya akan seperti berikut
![1](<Gambar/ATMh.png>)

### Flowchart

![1](<Gambar/ATMf.png>)
