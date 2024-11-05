saldo = 1000000
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
