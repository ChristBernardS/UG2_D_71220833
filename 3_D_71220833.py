jb = 0
diskon = 0
tot_diskon = 0
tot_harga = 0
mbyid = str(input('Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma): ')).split(', ')

for i in range(len(mbyid)):
    harga = int(input(f"Berapa harga barang {mbyid[jb]} ?: "))
    if harga < 25000000 and harga >= 10000000:
        diskon = harga*0.1
        tot_diskon += diskon
        tot_harga += harga
        jb += 1
        print(f"Harga {mbyid[jb]}\t\tRp. {harga}\tDiskon Rp. {diskon}")
    elif harga >= 25000000:
        diskon = harga*0.25
        tot_diskon += diskon
        tot_harga += harga
        jb += 1
        print(f"Harga {mbyid[jb]}\t\tRp. {harga}\tDiskon Rp. {diskon}")
    else:
        tot_harga += harga
        jb += 1
        print(f"Harga {mbyid[jb]}\t\tRp. {harga}\tDiskon Rp. {diskon}")

print(f"Total diskon yang anda dapatkan adalah sebesar: Rp. {tot_diskon}")
print(f"Total uang yang harus anda bayarkan adalah: Rp. {tot_harga-tot_diskon}")