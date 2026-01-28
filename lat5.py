from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target): pass
    @abstractmethod
    def info(self): pass

class Hero(GameUnit):
    def __init__(self, nama): self.nama = nama
    def serang(self, target): print(f"Hero {self.nama} menebas {target}!")
    def info(self): print(f"Saya adalah Hero: {self.nama}")


# Jawaban Tugas Analisis 5:

# Melanggar Kontrak: Jika method serang dihapus dari Hero, akan muncul Error: TypeError: Can't instantiate abstract class Hero with abstract method serang.
# Arti: Kita tidak bisa membuat objek dari clas yang "berhutang" method. Karena Hero berjanji mengikuti kontrak GameUnit, ia wajib punya method serang. Konsekuensinya: Program akan crash saat dijalankan, memaksa programmer untuk patuh.

# Mencetak Cetakan (unit = GameUnit()): Error akan muncul. GameUnit dilarang dibuat objek karena ia adalah konsep abstrak (hanya ide/template), bukan benda nyata. Gunanya adalah sebagai standar/kerangka bagi class-class turunannya.