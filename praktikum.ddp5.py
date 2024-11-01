#tugas no.1 ddp pekan 5
Kendaraan = ['supra bapak','motor',5000,'biru muda','15 roda']

Kendaraan.append('Rp 500.000.000')
Kendaraan.append('kendaraan pribadi')
Kendaraan.insert(2,'Hyunday')
print(Kendaraan)

print(type(Kendaraan))
print(type(Kendaraan[0]))
print(type(Kendaraan[1]))
print(type(Kendaraan[2]))
print(type(Kendaraan[3]))
print(type(Kendaraan[4]))
print(type(Kendaraan[5]))
print(type(Kendaraan[6]))
print(type(Kendaraan[7]))

#tugas no.2 ddp pekan 5
luas_bangun_datar = input('''
hitung luas apa?
    1. hitung luas persegi
    2. hitung luas lingkaran
    3. hitung luas segitiga
''')

match luas_bangun_datar:
    case '1':
        print('menghitung luas persegi')
        sisi = int(input('masukkan nilai sisi:'))
        hitung_luas_persegi = sisi**2
        print(f'jadi luas persegi dengan sisi {sisi} cm adalah', hitung_luas_persegi, 'cm²')
    case '2':
        print('menghitung luas lingkaran')
        pi = 3.14
        jari_jari = int(input('masukkan jari-jari'))
        hitung_luas_lingkaran = pi*jari_jari**2
        print(f'jadi luas lingkaran dengan jari-jari {jari_jari} cm adalah', hitung_luas_lingkaran, 'cm²')
    case '3':
        print('menghitung luas segitiga')
        alas = int(input('masukkan alas'))
        tinggi = int(input('masukkan tinggi'))
        hitung_luas_segitiga = 1/2*alas*tinggi
        print(f'jadi luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah', hitung_luas_segitiga, 'cm²')
    case _:
        print('pilihan tidak valid')