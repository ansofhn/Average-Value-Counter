print('\n','='*26,'\n','PENGHITUNG RATA-RATA NILAI','\n','='*26,'\n')
Totalsiswa=int(input("Jumlah Siswa   : "))
Siswa = 0
Jumlahnilai = 0
while Siswa < Totalsiswa:
    Nilaisiswa=int(input("|> Masukan Nilai  : "))
    Jumlahnilai += Nilaisiswa
    Siswa += 1
Ratarata = Jumlahnilai/Totalsiswa
print("\nJumlah Nilai   :",Jumlahnilai)
print("Rata-rata      :",Ratarata)