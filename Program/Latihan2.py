modal_awal = 100_000_000  # 100 juta dalam rupiah
keuntungan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.02]
total_keuntungan = 0
for bulan, persen_keuntungan in enumerate(keuntungan, start=1):
    laba_bulan = modal_awal * persen_keuntungan
    total_keuntungan += laba_bulan
    print(f"Bulan ke-{bulan}: Keuntungan = Rp {laba_bulan:,.0f}")
print(f"\nTotal keuntungan selama 8 bulan = Rp {total_keuntungan:,.0f}")