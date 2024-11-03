# bilanganBulat = [1,2,3,4,5,6,7,8,9]
# print(bilanganBulat)

# bilanganBulat.append("hello")
# print(bilanganBulat)

# menghapusElemen = bilanganBulat.pop(2)
# print(menghapusElemen)
# print(bilanganBulat)

# warna_lampu = input("Masukkan warna lampu :")

# match warna_lampu:
#     case "merah":
#         print("Berhenti")
#     case "kuning":
#         print("hati-hati")
#     case "hijau":
#         print("Jalan")
#     case _:
#         print("Input tidak valid")
        
        
# kendaraan = ["vario", "motor", 120, "hitam", 2]
# print(kendaraan)

# kendaraan.append("20juta")
# print(kendaraan)

# kendaraan.append("matic")
# print(kendaraan)

# kendaraan.insert(2, "Honda")
# print(kendaraan)
        
opsi_bangundatar = int(input
("""1. luas persegi 
2. luas lingkaran 
3. luas segitiga
Masukkan pilihan :"""))

match opsi_bangundatar:
    case 1:
        print("menghitung luas persegi")
        sisi = int(input("Masukkan nilai sisi:"))
        luas_persegi = sisi ** 2
        print(f"Luas Persegi dengan sisi {sisi} cm, adalah {luas_persegi}cm^2 ")
    case 2:
        print("menghitung luas lingkaran")
        π = (22/7)
        r = int(input("Masukkan nilai r:"))
        luas_lingkaran = π * r
        print(f"Luas Lingkaran dengan r {r} adalah {luas_lingkaran}cm^2 ")
    case 3 :
        print("menghitung luas segitiga")
        alas = int(input("Masukkan nilai alas:"))
        tinggi = int(input("Masukkan nilai tinggi:"))
        luas_segitiga = 1/2 * alas * tinggi
        print(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}cm^2 ")
    case _:
        print("salah pilih")
        