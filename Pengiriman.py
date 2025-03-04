def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    # Biaya dasar
    biaya = 10000
    
    # Tambahan biaya jika berat lebih dari 5 kg
    if berat > 5:
        biaya += 5000
    
    # Tambahan biaya jika jarak lebih dari 10 km
    if jarak > 10:
        biaya += 8000
    
    # Tambahan biaya untuk layanan express
    if express:
        biaya += 20000
    
    # Simpan biaya sebelum diskon
    biaya_sebelum_diskon = biaya
    
    # Diskon untuk member
    diskon = 0
    if member:
        diskon = biaya * 0.1  # Diskon 10%
        biaya *= 0.9
    
    return int(biaya), int(diskon), int(biaya_sebelum_diskon)  # Mengembalikan nilai dalam bentuk integer

# Fungsi untuk meminta input dari pengguna
def main():
    berat = float(input("Masukkan berat paket (kg): "))
    jarak = float(input("Masukkan jarak pengiriman (km): "))
    express = input("Apakah ingin menggunakan layanan express? (y/n): ").strip().lower() == "y"
    member = input("Apakah Anda member? (y/n): ").strip().lower() == "y"
    
    biaya_total, diskon, biaya_sebelum_diskon = hitung_biaya_pengiriman(berat, jarak, express, member)
    
    print(f"Biaya: Rp {biaya_sebelum_diskon}")
    if member:
        print(f"Diskon: Rp {diskon}")
    print(f"Total biaya: Rp {biaya_total}")

# Menjalankan program
if __name__ == "__main__":
    main()
