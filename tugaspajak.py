print("====================================================================")
print("                   Perhitungan Pajak Pak Leopold                    ")
print("====================================================================")
PenghasilanNetto=int(input("Penghasilan netto : "))
PenghasilanTidakKenaPajak=int(input("Penghasilan tidak kena pajak : "))
KreditPajak=int(input("Kredit pajak : "))
Pengguna=str(input("Nama pengguna : "))

if Pengguna == "Leopold":
    PenghasilanKenaPajak = int(PenghasilanNetto - PenghasilanTidakKenaPajak)
    Pajak1 = int(0.05 * 50000000) 
    Pajak2 = int(PenghasilanKenaPajak - 50000000)
    Pajak3 = int(0.15*Pajak2)
    PajakTerutang = int(Pajak1+Pajak3)
    PajakYangDibayar = int(PajakTerutang - KreditPajak)
else:
    print("Tidak Bayar Pajak")

print("Penghasilan Pak Leopold yang terkena pajak :Rp.", PenghasilanKenaPajak)
print("Total pajak terutang :Rp.", PajakTerutang)
print("Total pajak yang harus di bayar oleh Pak Leopold :Rp.", PajakYangDibayar)