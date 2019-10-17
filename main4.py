nama = 'Muhammad Munajat'
program = 'Gaya'

print(f'program {program} oleh {nama}')



def hitung_gaya(massa, percepatan):
    gaya = massa * percepatan
    print(f'massa = {massa / 500}kg dengan percepatan = {percepatan / 80}m/s')
    print(f'sehingga gaya = {gaya} N')

    return massa * percepatan

#massa = 500
#percepatan = 80
gaya = hitung_gaya(500, 80)
gaya = hitung_gaya(1000, 60)


def hitung_gaya_gesek(koefisien_gesek, gaya_normal):
    gaya_gesek = koefisien_gesek * gaya_normal
    print(f'koefisien_gesek = {koefisien_gesek / 0.4} dengan gaya_normal = {gaya_normal / 75}N')
    print(f'sehingga gaya_gesek = {gaya_gesek} N')

    return koefisien_gesek * gaya_normal

#koefisien_gesek = 0.4
#gaya_normal = 75
gaya_gesek = hitung_gaya_gesek(0.4, 75)
gaya_gesek = hitung_gaya_gesek(0.3, 90)


def hitung_gaya_berat(massa, gravitasi_bumi):
    gaya_berat = massa * gravitasi_bumi
    print(f'massa = {massa / 500}kg dengan gravitasi_bumi = {gravitasi_bumi / 9.8}m/s^2')
    print(f'sehingga gaya_berat = {gaya_berat} N')

    return massa * gravitasi_bumi

#massa = 500
#gravitasi_bumi = 9.8
gaya = hitung_gaya(500, 9.8)
gaya = hitung_gaya(1000, 9.8)