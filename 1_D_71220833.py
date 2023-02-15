# bagian menu
print(f"{15*'='} MAKANAN {15*'='}")
menu = {
    1. : 'Telur Bakar\t\t: Rp 7.000',
    2. : 'Lele Terbang Mas Bhe\t: Rp 10.000',
    3. : 'Es Coklat Lempu\t\t: Rp 5.000',
    4. : 'Es Doger Langensari\t: Rp 13.000'
}
for key, value in menu.items():
    print(f"{key} : {value}")
print('')

# bagian input
print(f"{20*'='} PESANAN {20*'='}")
makanan1_telur_bakar = int(input('Telur Bakar\t\t\t: '))
makanan2_Lele_Terbang_Mas_Bhe = int(input('Lele Terbang Mas Bhe\t\t: '))
makanan3_Es_Coklat_Lempu = int(input('Es Coklat Lempu\t\t\t: '))
makanan4_Es_Doger_Langensari = int(input('Es Doger Langensari\t\t: '))
print('')

# bagian proses
harga_makanan1 = 7000*makanan1_telur_bakar
harga_makanan2 = 10000*makanan2_Lele_Terbang_Mas_Bhe
harga_makanan3 = 5000*makanan3_Es_Coklat_Lempu
harga_makanan4 = 13000*makanan4_Es_Doger_Langensari

# bagian output
print(f"TOTAL TELUR BAKAR x {makanan1_telur_bakar}\t\t\t: Rp {harga_makanan1}")
print(f"TOTAL LELE TERBANG x {makanan2_Lele_Terbang_Mas_Bhe}\t\t\t: Rp {harga_makanan2}")
print(f"TOTAL ES COKLAT x {makanan3_Es_Coklat_Lempu}\t\t\t: Rp {harga_makanan3}")
print(f"TOTAL ES DOGER x {makanan4_Es_Doger_Langensari}\t\t\t: Rp {harga_makanan4}")
print(f"Jumlah total biaya yang harus dibayar adalah Rp {harga_makanan1+harga_makanan2+harga_makanan3+harga_makanan4}")