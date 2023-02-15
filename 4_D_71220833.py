data ={

}
n = 1

while True:
    print('')
    print(' !! Selamat datang di H+ GYM !!')
    print('Silahkan pilih menu dibawah ini:')
    print('1. Menambah Data\n2. Menampilkan Data\n3. Keluar')
    pilihan = int(input('Silahkan masukan pilihan yang anda inginkan: '))
    if pilihan == 1:
        nama_pelanggan = str(input('Masukkan nama pelanggan: '))
        jenis_member = str(input('Masukkan jenis member: '))
        print('Data sudah berhasil ditambahkan')
        if nama_pelanggan not in data.keys():
            data[nama_pelanggan] = jenis_member
    elif pilihan == 2:
        print(30*'-')
        print('Pelanggan\t\tMember:')
        for key, value in data.items():
            print(f"{n}.{key}\t\t{value}")
            n += 1
    elif pilihan == 3:
        print('\nSistem Berhenti...')
        break