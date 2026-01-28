from abc import ABC, abstractmethod

# --- 1. ABSTRACTION (Kerangka Dasar) ---
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar, stok):
        self.nama = nama
        self._harga_dasar = harga_dasar # Protected/Private convention
        self.__stok = stok              # Private (Encapsulation)

    # Abstract Method (Wajib di-override anak)
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

    # --- 2. ENCAPSULATION (Keamanan Data) ---
    # Getter untuk Stok
    def get_stok(self):
        return self.__stok

    # Method untuk mengubah stok dengan validasi
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    # Method bantu internal untuk mengurangi stok saat beli (opsional untuk logika real)
    def kurangi_stok(self, jumlah):
        if self.__stok >= jumlah:
            self.__stok -= jumlah
            return True
        return False

# --- 3. INHERITANCE (Pewarisan) ---
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, processor):
        super().__init__(nama, harga_dasar, stok)
        self.processor = processor

    # --- 4. POLYMORPHISM (Override Method) ---
    def tampilkan_detail(self):
        return f"[LAPTOP] {self.nama} | Proc: {self.processor}"

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self._harga_dasar # 10%
        harga_satuan = self._harga_dasar + pajak
        return harga_satuan * jumlah, pajak * jumlah

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, kamera):
        super().__init__(nama, harga_dasar, stok)
        self.kamera = kamera

    # --- 4. POLYMORPHISM (Override Method) ---
    def tampilkan_detail(self):
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}"

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self._harga_dasar # 5%
        harga_satuan = self._harga_dasar + pajak
        return harga_satuan * jumlah, pajak * jumlah

# --- Fitur Transaksi (Fungsi Luar Class) ---
def proses_transaksi(daftar_belanja):
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    nomor = 1

    for item in daftar_belanja:
        objek_barang = item['barang']
        jumlah_beli = item['jumlah']

        # Validasi stok sederhana
        if objek_barang.get_stok() >= jumlah_beli:
            # Hitung harga (Polymorphism berjalan di sini)
            subtotal, total_pajak = objek_barang.hitung_harga_total(jumlah_beli)

            # Tampilkan Detail
            print(f"{nomor}. {objek_barang.tampilkan_detail()}")
            print(f"   Harga Dasar: Rp {objek_barang._harga_dasar:,.0f} | Pajak: Rp {total_pajak:,.0f}")
            print(f"   Beli: {jumlah_beli} unit | Subtotal: Rp {subtotal:,.0f}")
            total_tagihan += subtotal
            nomor += 1
        else:
            print(f"{nomor}. Gagal beli {objek_barang.nama}. Stok tidak cukup!")

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("----------------------------------------")

# --- SKENARIO UTAMA (Main Program) ---

print("--- SETUP DATA ---")
# 1. Admin membuat data produk
laptop_rog = Laptop("ROG Zephyrus", 20000000, 0, "Ryzen 9")
hp_iphone = Smartphone("iPhone 13", 15000000, 0, "12MP")

# 2. Admin mengisi stok (Uji Validasi Encapsulasi)
laptop_rog.tambah_stok(10)      # Berhasil
hp_iphone.tambah_stok(-5)       # Gagal (Negatif)
hp_iphone.tambah_stok(20)       # Berhasil

# 3. User membeli (Simulasi Keranjang Belanja)
# Format keranjang: List of dictionary
keranjang_user = [
    {'barang': laptop_rog, 'jumlah': 2},
    {'barang': hp_iphone, 'jumlah': 1}
]

# 4. Proses Transaksi
proses_transaksi(keranjang_user)