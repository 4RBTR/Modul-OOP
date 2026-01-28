Jawaban Tugas Analisis 5:

Melanggar Kontrak: Jika method serang dihapus dari Hero, akan muncul Error: TypeError: Can't instantiate abstract class Hero with abstract method serang.

Arti: Kita tidak bisa membuat objek dari class yang "berhutang" method. Karena Hero berjanji mengikuti kontrak GameUnit, ia wajib punya method serang. Konsekuensinya: Program akan crash saat dijalankan, memaksa programmer untuk patuh.

Mencetak Cetakan (unit = GameUnit()): Error akan muncul. GameUnit dilarang dibuat objek karena ia adalah konsep abstrak (hanya ide/template), bukan benda nyata. Gunanya adalah sebagai standar/kerangka bagi class-class turunannya.

___________________________________________________________________________________________________________________________________________________

Latihan 6: Polymorphism
Jawaban Tugas Analisis 6:

Uji Skalabilitas (Menambah Class Healer): Program akan berjalan lancar. Kita tidak perlu mengubah kode looping sama sekali.

Keuntungan: Memudahkan maintenance dan pengembangan. Jika ada 100 jenis hero baru, kode utama permainan (logika looping pertarungan) tidak perlu diedit satu per satu.

Konsistensi Penamaan: Jika nama method di Archer diubah jadi tembak_panah, akan terjadi Error AttributeError saat loop berjalan pada giliran Archer.

Mengapa harus sama? Karena Polymorphism bekerja dengan prinsip "Panggil nama yang sama, hasil beda". Pemanggil (loop) hanya tahu perintah serang(). Jika namanya beda, perintah itu tidak dikenali.