#NO 1.A
class Pesan(object):
    """
        Sebuah class bernama Pesan ,untuk memahami konsep Class dan Object."""
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, kata):
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False

#NO 1.B
    def hitungKonsonan(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() not in vowel :
                jml+=1
        return jml
    
#NO 1.C
    def hitungVokal(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() in vowel :
                jml+=1
        return jml
    
#NO 2.A
    """Class Mahasiswa dari class Manusia"""
class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2


class Mahasiswa(Manusia):
    """Class Mahasiswa dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulannya."
        return s
    def ambilNama(self):
        print (self.nama)
    def ambilNIM(self):
        print (self.NIM)
    def ambilUangSaku(self):
        print (self.uangsaku)
    def makan(self,s):
        """Metode ini menutupi makan nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru makan",s,"sambil belajar.")
        self.keadaan="Kenyang bro"


#NO 2.B
    def perbaruiKotaTinggal(self, baru):
        self.kotaTinggal = baru
#NO 2.C
    def tambahUangSaku(self, uang):
        self.uangsaku = self.uangsaku + uang
#NO 3
    
##x = input("Masukkan Nama : ")
##y = input("Masukkan NIM  : ")
##z = input("Masukkan Kota Tinggal  : ")INGAT DATA HARUS BERUPA STRING
##a = input("Masukkan Uang : ")
## mhs = Mahasiswa(a,b,c,d)
## mhs.ambilNama()
## mhs.ambilNIM()
## mhs.ambilKotaTinggal()
## mhs.ambilUangSaku()

#NO 4
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
#NO 5
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
#NO 6
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,nama,no_induk,kelas,alamat):
        """Metode inisialisasi ini menyempurnakan metode inisiasi di clas manusia."""
        self.nama = nama
        self.no = no_induk
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        a = "Nama : "+self.nama+'\n'+"no induk : "+str(self.no)+'\n'+"tinggal di : "+self.alamat+'\n'+"kelas : "+str(self.kelas)
        print (a)
    def ambilNama(self):
        print (self.nama)
    def ambilNoInduk(self):
        print (self.no)
    def ambilKelas(self):
        print (self.kelas)
    def ambilAlamat(self):
        print (self.alamat)
#NO 7
class MhsTIF(Manusia):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpy(self):
        print('ini python')
