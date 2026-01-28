class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}!")


class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power) # Memanggil constructor Parent
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


# Jawaban Tugas Analisis 3:

# Eksperimen Fungsi super(): Jika super().__init__(...) dihapus, akan muncul Error AttributeError: 'Mage' object has no attribute 'name'
# Mengapa Error? Karena atribut name, hp, dan attack_power didefinisikan di dalam __init__ milik Parent (Hero). Jika kita tidak memanggilnya menggunakan super(), maka atribut-atribut tersebut tidak pernah dibuat untuk objek Mage
# Peran super(): Menghubungkan class Anak dengan Parent, memungkinkan Anak untuk menjalankan kode inisialisasi yang sudah ditulis di Parent agar tidak perlu ditulis ulang (DRY - Don't Repeat Yourself).
