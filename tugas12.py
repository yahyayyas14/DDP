# Parent class Animal
class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info(self):
        return f"{self.name} makan {self.makanan}, hidup di {self.hidup}, dan berkembang biak dengan cara {self.berkembang_biak}"

# Child class Burung
class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, sayap, jenis_burung):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.sayap = sayap
        self.jenis_burung = jenis_burung

    def terbang(self):
        return f"{self.name} bisa terbang dengan sayap {self.sayap}"

# Child class Ikan
class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_ikan, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_ikan = jenis_ikan
        self.habitat = habitat

    def berenang(self):
        return f"{self.name} berenang di habitat {self.habitat}"

# Child class Ular
class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang, berbahaya):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.berbahaya = berbahaya

    def berbisa(self):
        return f"{self.name} adalah ular yang {'berbahaya' if self.berbahaya else 'tidak berbahaya'}, dengan panjang {self.panjang} meter."

# Membuat objek dari setiap class child

# Objek untuk class Burung
burung1 = Burung("Elang", "daging", "udara", "bertelur", "lebar", "Elang Eropa")
burung2 = Burung("Pipit", "biji-bijian", "darat", "bertelur", "kecil", "Pipit Hutan")

# Objek untuk class Ikan
ikan1 = Ikan("Nemo", "plankton", "laut", "bertelur", "ikan Clownfish", "terumbu karang")
ikan2 = Ikan("Ikan Mas", "pelet", "kolam", "beranak", "ikan Mas", "kolam air tawar")

# Objek untuk class Ular
ular1 = Ular("King Cobra", "mamalia kecil", "darat", "bertelur", 5.5, True)
ular2 = Ular("Boa", "mamalia kecil", "darat", "beranak", 3.0, False)

# Menampilkan informasi setiap objek
print(burung1.info())
print(burung1.terbang())
print(burung2.info())
print(burung2.terbang())

print(ikan1.info())
print(ikan1.berenang())
print(ikan2.info())
print(ikan2.berenang())

print(ular1.info())
print(ular1.berbisa())
print(ular2.info())
print(ular2.berbisa())
