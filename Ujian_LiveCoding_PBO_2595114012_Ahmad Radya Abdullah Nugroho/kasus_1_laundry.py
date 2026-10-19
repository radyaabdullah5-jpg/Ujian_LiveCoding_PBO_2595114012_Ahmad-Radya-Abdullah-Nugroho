class TagihanLaundry:
    def __init__(self, nama_pelanggan, jenis_layanan, berat_cucian):
        self.nama_pelanggan = nama_pelanggan
        self.jenis_layanan = jenis_layanan
        self.berat_cucian = berat_cucian
        self.tarif_per_kg = 0
        self.subtotal = 0
        self.persen_diskon = 0
        self.nominal_diskon = 0
        self.total_bayar = 0

    def hitung_tagihan(self):
        # Tentukan tarif berdasarkan jenis layanan
        if self.jenis_layanan.lower() == "reguler":
            self.tarif_per_kg = 8000
        elif self.jenis_layanan.lower() == "kilat":
            self.tarif_per_kg = 12000

        self.subtotal = self.tarif_per_kg * self.berat_cucian

        # Tentukan persentase diskon berdasarkan berat
        if self.berat_cucian >= 10:
            self.persen_diskon = 15
        elif self.berat_cucian >= 5:
            self.persen_diskon = 10
        else:
            self.persen_diskon = 0

        self.nominal_diskon = self.subtotal * (self.persen_diskon / 100)
        self.total_bayar = self.subtotal - self.nominal_diskon

    def cetak_nota(self):
        print("\n=== NOTA PEMBAYARAN LAUNDRY ===")
        print(f"Pelanggan     :  {self.nama_pelanggan}")
        print(f"Layanan       :  {self.jenis_layanan.capitalize()} (Rp{self.tarif_per_kg:,}/kg)".replace(',','.'))
        print(f"Berat         :  {self.berat_cucian} kg")
        print(f"Subtotal      :  Rp{int(self.subtotal):,}".replace(',','.'))
        print(f"Diskon        :  {self.persen_diskon}%")
        print(f"Potongan      :  Rp{int(self.nominal_diskon):,}".replace(',','.'))
        print(f"Total Bayar   :  Rp{int(self.total_bayar):,}".replace(',','.'))
        print("=====")


def main():
    print("=== LAUNDRY CLEAN & FRESH ===")
    nama = input("Nama pelanggan ")

    # validasi input Jenis Layanan
    while True:
        layanan = input("jenis layanan : ")
        if layanan.lower() in ("reguler", "kilat"):
            break
        print("layanan tifak valid! Pilih 'Reguler' atau 'Kilat'.")

    # validasi input Berat Cucian
    while True:
        try:
            berat = float(input("Berat cucian : "))
            if berat > 0:
                break
            print("Berat cucian harus lebih dari 0!")
        except ValueError:
            print("input harus berupa angka!")

    # Buat objek dan panggil method
    laundry = TagihanLaundry(nama, layanan, berat)
    laundry.hitung_tagihan()
    laundry.cetak_nota()

if __name__ == "__main__":
    main()