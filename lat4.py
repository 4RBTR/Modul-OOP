class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal  # Private

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# Jawaban Tugas Analisis 4:

# Percobaan Hacking (hero1._Hero__hp): Nilai HP akan muncul (tidak error). Python menggunakan teknik Name Mangling di mana variabel private __hp sebenarnya diubah namanya menjadi _NamaClass__hp. Namun, standar pemrograman yang baik melarang ini karena melanggar prinsip enkapsulasi; kita seharusnya menghormati privasi data agar program aman dan terprediksi.

# Uji Validasi (Tanpa logika if): Jika validasi dihapus, hero1.set_hp(-100) akan membuat HP menjadi negatif. Pentingnya Setter: Untuk menjaga integritas data. Setter bertindak sebagai "satpam" yang memastikan data yang masuk akal (valid) saja yang disimpan, mencegah bug aneh seperti nyawa negatif dalam game.