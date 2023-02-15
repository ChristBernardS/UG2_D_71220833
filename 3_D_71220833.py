mbyid = str(input('Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma): ')).split(', ')

harga1 = int(input(f"Berapa harga barang {mbyid[0]} ?: "))
if harga1 >= 10000000:
    print(f"Harga {mbyid[0]}\t\tRp. {harga1}\tDiskon Rp. {(harga1//10000000)*(0.1*harga1)}")
else:
    print(f"Harga {mbyid[0]}\t\tRp. {harga1}\tDiskon Rp. 0")

harga2 = int(input(f"Berapa harga barang {mbyid[1]} ?: "))
if harga2 >= 10000000:
    print(f"Harga {mbyid[1]}\t\tRp. {harga2}\tDiskon Rp. {(harga2//10000000)*(0.1*harga2)}")
else:
    print(f"Harga {mbyid[1]}\t\tRp. {harga2}\tDiskon Rp. 0")

harga3 = int(input(f"Berapa harga barang {mbyid[2]} ?: "))
if harga3 >= 10000000:
    print(f"Harga {mbyid[2]}\t\tRp. {harga3}\tDiskon Rp. {(harga3//10000000)*(0.1*harga3)}")
else:
    print(f"Harga {mbyid[2]}\t\tRp. {harga3}\tDiskon Rp. 0")

harga4 = int(input(f"Berapa harga barang {mbyid[3]} ?: "))
if harga4 >= 10000000:
    print(f"Harga {mbyid[3]}\t\tRp. {harga4}\tDiskon Rp. {(harga4//10000000)*(0.1*harga4)}")
else:
    print(f"Harga {mbyid[3]}\t\tRp. {harga4}\tDiskon Rp. 0")

total_harga = harga1+harga2+harga3+harga4
total_diskon = 0
for i in range(0):
    if harga1 >= 10000000:
        total_diskon += harga1*0.1
    else:
        total_diskon += 0
    if harga2 >= 10000000:
        total_diskon += harga2*0.1
    else:
        total_diskon += 0
    if harga3 >= 10000000:
        total_diskon += harga3*0.1
    else:
        total_diskon += 0
    if harga4 >= 10000000:
        total_diskon += harga4*0.1
    else:
        total_diskon += 0

if total_diskon >= 25000000:
    total_diskon = (total_diskon//25000000)*(total_diskon*0.25)
else:
    total_diskon += 0

print(f"Total diskon yang anda dapatkan adalah sebesar: Rp. {total_diskon}")
print(f"Total uang yang harus anda bayarkan adalah: Rp. {total_harga-total_diskon}")