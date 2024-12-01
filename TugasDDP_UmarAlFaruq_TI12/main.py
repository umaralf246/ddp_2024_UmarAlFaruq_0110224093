from mtk import *
from ruang import *
from luas import *

def menu():
    while True:
        print("Pilih program^_^")
        print("1. Operasi aritmatika")
        print("2. Luas bangun datar")
        print("3. Luas permukaan bangun ruang")
        print("4. Batal")


        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            PerhitunganAritmatika()
        elif pilihan == 2:
            LuasBangunDatar()
        elif pilihan == 3:
            LuasPermukaanBangunRuang()
        elif pilihan == 4:
            break
        else:
            ("pilihan tidak ada!")

    

def PerhitunganAritmatika():
    while True:
        print("pilih operasi aritmatika")
        print("1. penjumlahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        print("5. pangkat")
        print("6. Kembbali")
        pilihan = int(input("masukkan pilihan : "))

        if pilihan == 1:
            a = int(input("masukkan angka pertama : "))
            b = int(input("masukkan angka kedua : "))
            print ("hasilnya adalah : ",tambah (a, b))
        elif pilihan == 2:
            a = int(input("masukkan angka pertama : "))
            b = int(input("masukkan angka kedua : "))
            print ("hasilnya adalah : ", kurang(a, b))

        elif pilihan == 3:
            a = int(input("masukkan angka pertama : "))
            b = int(input("masukkan angka kedua : "))
            print ("hasilnya adalah : ", kali(a, b))

        elif pilihan == 4:
            a = int(input("masukkan angka pertama : "))
            b = int(input("masukkan angka kedua : "))
            print( "hasilnya adalah : ", bagi(a, b))
        elif pilihan == 5:
            a = int(input("masukkan angka pertama : "))
            b = int(input("masukkan angka kedua : "))
            print("hasilnya adalah : ", pangkat(a, b))
        elif pilihan == 6:
            break
        else:
            print("pilihan tidak ada")

def LuasBangunDatar():
    while True:
        print("pilih bangun datar")
        print("1. persegi")
        print("2. segitiga")
        print("3. lingkaran")
        print("4. trapesium")
        print("5. persegi panjang")
        print("6. Kembali")
        pilihan=int(input("Masukan pilihan : "))

        if pilihan == 1:
            s = int(input("masukkan sisi : "))
            print("luas persegi adalah : ", persegi(s))

        elif pilihan == 2:
            a = int(input("masukkan alas : "))
            t = int(input("masukkan tinggi : "))
            print("luas segitiga adalah : ", segitiga(a, t))

        elif pilihan == 3:
            r = int(input("masukkan jari-jari : "))
            print("luas lingkaran adalah : ", lingkaran(r))
     
        elif pilihan == 4:
            a = int(input("masukkan alas : "))
            b = int(input("masukkan alas : "))
            t = int(input("masukkan tinggi : "))
            print("luas trapesium adalah : ", trapesium(a, b, t))
        elif  pilihan == 5:
            p = int(input("masukan panjang: "))
            t = int(input("masukan tinggi: "))
            print("luas persegi panjang adalah: ", persegi_panjang(p,t))
        elif pilihan == 6:
            break
        else:
            print("pilihan tidak ada")        

def LuasPermukaanBangunRuang():
    while True:
        print("pilih bangun ruang")
        print("1. kubus")
        print("2. balok")
        print("3. tabung")
        print("4. kerucut")
        print("5. bola")
        print("6. Kembali")
        pilihan=int(input("Masukan pilihan : "))
        if pilihan == 1:
            s = int(input("masukkan sisi : "))
            print("luas permukaan kubus adalah : ", kubus(s))
        elif pilihan == 2:
            p = int(input("masukkan panjang : "))
            l = int(input("masukkan lebar : "))
            t = int(input("masukkan tinggi : "))
            print("luas permukaan balok adalah : ", balok(p, l, t))
        elif pilihan == 3:
            r = int(input("masukkan jari-jari : "))
            t = int(input("masukkan tinggi : "))
            print("luas permukaan tabung adalah : ", tabung(r, t))
        elif pilihan == 4:
            r = int(input("masukkan jari-jari : "))
            t = int(input("masukkan tinggi : "))
            print("luas permukaan kerucut adalah : ", kerucut(r, s))
        elif pilihan == 5:
            r = float(input("masukkan jari-jari : "))
            print("luas permukaan bola adalah : ", bola(r))
        elif pilihan == 6:
            break
        else:
            print("pilihan tidak ada")
    


if __name__ == "__main__":
    menu()
    

