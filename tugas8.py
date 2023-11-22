def tampilkan_profil(nama,alamat,gender,umur):
    print("profil")
    print("Nama:",nama)
    print("Alamat:",alamat)
    print("Gender:",gender)
    print("Umur:",umur)
tampilkan_profil("Dayati","jalan material no.39","perempuan","18")

def cek_kelulusan(nilai):
    if nilai <60:
        print("gagal")
    elif 61 <= nilai<= 70:
        print("Baik")
    elif 71 <= nilai <= 80:
        print("sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")

    else:
        print("Tidak Lulus")
    cek_kelulusan(60)

    def ganjil(bilangan):
        for i in range (1,bilangan+1,2):
            print(i)
    #memanggil 
    ganjil(9)