# bagian input
nomorHP_anda = str(input('Masukkan Nomor Telepon : '))

# bagian proses
nomorHP_anda = list(nomorHP_anda)

# bagain output
if nomorHP_anda[0:4] == ['0','8','1','4']:
    print('Anda menggunakan operator Telkomsel')
elif nomorHP_anda[0:4] == ['0','8','1','6']:
    print('Anda menggunakan operator Indosat')
else:
    print('Operator anda tidak diketahui')

if int(nomorHP_anda[-1])%2 == 0:
    print('Nomor anda berakhiran genap')
elif int(nomorHP_anda[-1])%2 == 1:
    print('Nomor anda berakhiran ganjil')
else:
    print('error')