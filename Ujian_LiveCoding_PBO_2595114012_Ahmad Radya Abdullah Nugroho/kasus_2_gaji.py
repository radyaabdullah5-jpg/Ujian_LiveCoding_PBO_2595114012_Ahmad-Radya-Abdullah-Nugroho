class GajiKaryawan:
    def __init__(self, id_karyawan, nama, jam_kerja):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.jam_kerja = jam_kerja
        self.jam_reguler = 0
        self.jam_lembur = 0
        self.gaji_pokok = 0
        self.upah_lembur = 0
        self.gaji_kotor = 0
        self.pajak = 0
        self.gaji_bersih = 0

    def hitung_gaji(self):
        # Perhitungan jam dan gaji pokok/lembur
        if self.jam_kerja > 40:
            self.jam_reguler = 40
            self.jam_lembur = self.jam_kerja - 40
        else:
            self.jam_reguler = self.jam_kerja
            self.jam_lembur = 0

        self.gaji_pokok = self.jam_reguler * 30000
        self.upah_lembur = self.jam_lembur * 45000
        self.gaji_kotor = self.gaji_pokok + self.upah_lembur

        # Perhitungan pajak
        if self.gaji_kotor >= 1500000:
            self.pajak = self.gaji_kotor * 0.05
        else:
            self.pajak = 0

        self.gaji_bersih = self.gaji_kotor - self.pajak

    def cetak_slip(self):
        print('\n=== SLIP GAJI KARYAWAN ===')
        print(f"ID karyawan    :  {self.id_karyawan}")
        print(f"Nama           :  {self.nama}")
        print(f"Jam Reguler    :  {self.jam_reguler} jam (Rp{self.gaji_pokok:,})".replace(',','.'))
        print(f"Jam Lembur     :  {self.jam_lembur} jam (Rp{self.upah_lembur:,})".replace(',','.'))
        print(f"Gaji Kotor     :  Rp{self.gaji_kotor:,}".replace(',','.'))
        print(f"Pajak (5%)     :  Rp{int(self.pajak):,}".replace(',','.'))
        print(f"Gaji Bersih    :  Rp{int(self.gaji_bersih):,}".replace(',','.'))


def main():
    print("=== SISTEM PENGGAJIAN HONORER ===")
    id_karyawan = input("ID karyawan: ")
    nama = input("Nama       : ")

    # Validasi Jam Kerja (1 - 80 jam)
    while True:
        try:
            jam_kerja = int(input("Jam Kerja   : "))
            if 1 <= jam_kerja <= 80:
                break
            print("Jam kerja harus berada dalam rentang 1 sampai 80 jam!")
        except ValueError:
            print("Input jam kerja harus berupa angka bulat!")

    # Buat objek dan panggil method
    karyawan = GajiKaryawan(id_karyawan, nama, jam_kerja)
    karyawan.hitung_gaji()
    karyawan.cetak_slip()


if __name__ == "__main__":
    main()
