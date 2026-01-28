class Hero:
    # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name          # Nama Hero
        self.hp = hp              # Nyawa (Health Point)
        self.attack_power = attack_power  # Kekuatan Serangan

    # Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    # Method menyerang
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method diserang
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# -- Main Program --
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)
hero1.info()
hero2.info()

#latihan 1
#Apa yang terjadi jika hero1hp diubah menjadi 500?
#  Nilai HP akan berubah menjadi 500. Karena atribut hp bersifat public (tidak diprivate), kita bisa mengubahnya secara langsung dari luar class. print(hero1.hp) akan menghasilkan output 500.


#latihan 2
#Mengapa parameter lawan menerima objek utuh penting?
#Penting agar method serang bisa mengakses seluruh data (seperti lawan.name) dan memanggil method milik lawan (seperti lawan.diserang()). Jika hanya string nama yang dikirim, kita tidak bisa mengurangi HP lawan tersebut karena kita tidak memiliki akses ke "tubuh" (objek) lawan yang sebenarnya.