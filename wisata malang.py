wisata_malang = [
    {
        "nama": "Jatim Park 1",
        "harga": 100000,
        "deskripsi": "Taman bermain dan edukasi yang cocok untuk keluarga.",
        "alamat": "Jl. Dewi Sartika, Kec.Batu, Malang, Jawa Timur",
        "jam_buka": "09:00 - 17:00"
    },
    {
        "nama": "Batu Night Spectacular",
        "harga": 75000,
        "deskripsi": "Wahana hiburan malam dengan atraksi dan lampu spektakuler.",
        "alamat": "Jl.  Hayam Wuruk No 1, Oro-Oro Ombo, Kec.Batu, Malang",
        "jam_buka": "15:00 - 23:00"
    },
    {
        "nama": "Museum Angkut",
        "harga": 100000,
        "deskripsi": "Museum transportasi dengan koleksi kendaraan dari berbagai era.",
        "alamat": "Jl. Terusan Sultan Agung No.2, Kec.Batu, Malang",
        "jam_buka": "12:00 - 20:00"
    },
    {
        "nama": "Kebun Apel",
        "harga": 25000,
        "deskripsi": "Kebun wisata di mana pengunjung dapat memetik apel segar.",
        "alamat": "Desa Punten, Kec.Batu, Malang",
        "jam_buka": "08:00 - 16:00"
    }
]

# untuk menampilkan daftar tempat wisata
def tampilkan_wisata():
    print("Daftar Tempat Wisata di Malang:")
    for i, wisata in enumerate(wisata_malang, start=1):
        print(f"{i}. {wisata['nama']} - Rp{wisata['harga']}")

# untuk menambahkan tempat wisata
def tambah_wisata():
    nama = input("Masukkan nama tempat wisata: ")
    harga = int(input("Masukkan harga tiket masuk: "))
    deskripsi = input("Masukkan deskripsi tempat wisata: ")
    alamat = input("Masukkan alamat tempat wisata: ")
    jam_buka = input("Masukkan jam buka: ")
    wisata_malang.append({
        "nama": nama,
        "harga": harga,
        "deskripsi": deskripsi,
        "alamat": alamat,
        "jam_buka": jam_buka
    })
    print(f"{nama} berhasil ditambahkan ke daftar wisata!")

# untuk mencari tempat wisata
def cari_wisata():
    keyword = input("Masukkan nama tempat wisata yang ingin dicari: ").lower()
    hasil = [wisata for wisata in wisata_malang if keyword in wisata["nama"].lower()]
    if hasil:
        print("Hasil pencarian:")
        for wisata in hasil:
            print(f"Nama: {wisata['nama']}")
            print(f"Harga: Rp{wisata['harga']}")
            print(f"Deskripsi: {wisata['deskripsi']}")
            print(f"Alamat: {wisata['alamat']}")
            print(f"Jam Buka: {wisata['jam_buka']}")
    else:
        print("Tempat wisata tidak ditemukan.")

# untuk mengupdate tempat wisata
def update_wisata():
    tampilkan_wisata()
    pilihan = int(input("Masukkan nomor tempat wisata yang ingin diupdate: "))
    if 1 <= pilihan <= len(wisata_malang):
        wisata = wisata_malang[pilihan - 1]
        print(f"Mengupdate {wisata['nama']}:")
        nama_baru = input("Masukkan nama baru (Jika ingin di ubah): ")
        harga_baru = input("Masukkan harga baru (Jika ingin di ubah): ")
        deskripsi_baru = input("Masukkan deskripsi baru (Jika ingin di ubah): ")
        alamat_baru = input("Masukkan alamat baru (Jika ingin di ubah): ")
        jam_buka_baru = input("Masukkan jam buka baru (Jika ingin di ubah): ")

        if nama_baru:
            wisata["nama"] = nama_baru
        if harga_baru:
            wisata["harga"] = int(harga_baru)
        if deskripsi_baru:
            wisata["deskripsi"] = deskripsi_baru
        if alamat_baru:
            wisata["alamat"] = alamat_baru
        if jam_buka_baru:
            wisata["jam_buka"] = jam_buka_baru
        
        print(f"Data {wisata['nama']} berhasil diperbarui!")
    else:
        print("Pilihan tidak valid.")

# untuk menghapus tempat wisata
def hapus_wisata():
    tampilkan_wisata()
    pilihan = int(input("Masukkan nomor tempat wisata yang ingin dihapus: "))
    if 1 <= pilihan <= len(wisata_malang):
        wisata_terhapus = wisata_malang.pop(pilihan - 1)
        print(f"{wisata_terhapus['nama']} berhasil dihapus dari daftar wisata!")
    else:
        print("Pilihan tidak valid.")


# Menu utama
def menu():
    while True:
        print("=== Sistem Informasi Wisata Malang ===")
        print("1. Lihat daftar tempat wisata")
        print("2. Tambah tempat wisata")
        print("3. Hapus tempat wisata")
        print("4. Update tempat wisata")
        print("5. Cari tempat wisata")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == "1":
            tampilkan_wisata()
        elif pilihan == "2":
            tambah_wisata()
        elif pilihan == "3":
            hapus_wisata()
        elif pilihan == "4":
            update_wisata()
        elif pilihan == "5":
            cari_wisata()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem informasi wisata di daerah Malang!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
menu()
