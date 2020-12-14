class bioskop:
    judul = ''
    nama = ''
    jam = ''

    def __init__(self,judul):
        self.judul = judul
    def get_nama (self,nama):
        self.nama = nama
    def get_jam(self,jam):
        self.jam = jam

a = bioskop('plastic memories')
a.get_nama('Nasrijal')
a.get_jam('08:00')

print('judul film : %s\nnama : %s \njam tayang : %s' % (a.judul,a.nama,a.jam))