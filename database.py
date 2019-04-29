import pymysql

class Database:
    def __init__(self):
        host = # Host 
        user = #Kullanıcı Adı
        password = #şifre
        db = #Veritabanı ismi
        
        self.con = pymysql.connect(
            host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

#-------------- Öğrenci ---------------
    def ogrenci(self):
        self.cur.execute("select * from klasik_ogrenci")
        result = self.cur.fetchall()
        return result
    
    def dgsogrenci(self):
        self.cur.execute("select * from dgs_ogrenci")
        result = self.cur.fetchall()
        return result

    def numaraekle(self,numara):
        self.cur.execute("insert into ogrenci (ogrenci_numara) values (%s)", numara)
        self.con.commit()
    
    def ogrenciekle(self,ogrenci_bilgisi):
        self.cur.execute(
            "INSERT INTO klasik_ogrenci (ogrenci_numara, ogrenci_isim, ogrenci_soyisim,ogrenci_ogretim,staj_toplam_gun) VALUES (%s, %s, %s, %s, %s)", ogrenci_bilgisi)
        self.con.commit()
 
    def numarasil(self,numara):
        self.cur.execute("delete from ogrenci where ogrenci_numara=%s", numara)
        self.con.commit()
        
    def ogrencisil(self,numara):
        self.cur.execute(
            "delete from klasik_ogrenci where ogrenci_numara=%s", numara)
        self.con.commit()

    def ogrencilistele(self, numara):
        self.cur.execute(
            "SELECT * FROM klasik_ogrenci WHERE ogrenci_numara=%s", numara)
        result = self.cur.fetchone()
        return result

    def dgsogrencilistele(self, numara):
        self.cur.execute(
            "SELECT * FROM dgs_ogrenci WHERE ogrenci_numara=%s", numara)
        result = self.cur.fetchone()
        return result
        
    
    def ogrenciduzenle(self,data):
        self.cur.execute(
            "UPDATE klasik_ogrenci SET ogrenci_isim=%s, ogrenci_soyisim=%s, ogrenci_ogretim=%s  WHERE ogrenci_numara=%s", data)
        self.con.commit()

    def ogrencistajlistele(self,numara):
        self.cur.execute("select * from staj_mulakat where ogrenci_numara=%s",numara)
        result = self.cur.fetchall()
        return result

    def dgsogrenciekle(self,ogrenci_bilgisi):
        self.cur.execute(
            "INSERT INTO dgs_ogrenci (ogrenci_numara, ogrenci_isim, ogrenci_soyisim,ogrenci_ogretim,staj_toplam_gun,onceki_okul) VALUES (%s, %s, %s, %s,%s,%s)", ogrenci_bilgisi)
        self.con.commit()

    def dgsogrencisil(self,numara):
        self.cur.execute(
            "delete from dgs_ogrenci where ogrenci_numara=%s", numara)
        self.con.commit()

    def dgsogrenciduzenle(self,data):
        self.cur.execute(
            "UPDATE dgs_ogrenci SET ogrenci_isim=%s, ogrenci_soyisim=%s, ogrenci_ogretim=%s, onceki_okul=%s WHERE ogrenci_numara=%s", data)
        self.con.commit()

    def dgsogrencistajlistele(self,numara):
        self.cur.execute("select * from staj_mulakat where ogrenci_numara=%s",numara)
        result = self.cur.fetchall()
        return result

#-------Akademisyen-------------
    def akademisyen(self):
        self.cur.execute("select * from komisyon")
        result = self.cur.fetchall()
        return result

    def akademisyenekle(self,akademisyen_bilgisi):
        self.cur.execute(
            "INSERT INTO komisyon (komisyon_numara, komisyon_isim, komisyon_soyisim,komisyon_unvan) VALUES (%s, %s, %s, %s)", akademisyen_bilgisi)
        self.con.commit()

    def komisyonlistele(self, numara):
        self.cur.execute(
            "SELECT * FROM komisyon WHERE komisyon_numara=%s", numara)
        result = self.cur.fetchone()
        return result

    def komisyonduzenle(self,data):
        self.cur.execute(
            "UPDATE komisyon SET komisyon_isim=%s, komisyon_soyisim=%s, komisyon_unvan=%s   WHERE komisyon_numara=%s", data)
        self.con.commit()
    

    def komisyonsil(self,numara):
        self.cur.execute(
            "delete from komisyon where komisyon_numara=%s", numara)
        self.con.commit()

#---------------Staj-------------------
    def staj(self):
        self.cur.execute("select * from staj_mulakat")
        result = self.cur.fetchall()
        return result

    def stajekle(self,staj_bilgisi):
        self.cur.execute(
            "INSERT INTO staj_mulakat (ogrenci_numara, staj_baslama_tarihi, staj_bitis_tarihi,staj_sehir,staj_konu,staj_kurum,staj_toplam_gun,staj_sinif,staj_kabul_edilen_gun,mulakat_kontrol,mulakat_tarih,mulakat_saat,komisyon_uye_1,komisyon_uye_2,devam,caba_ve_calisma,isi_vaktinde_yapma,amire_karsi_davranis,is_arkadasina_karsi_davranis,proje,duzen,sunum,icerik,mulakat) VALUES (%s,%s ,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )", staj_bilgisi)                                      
        self.con.commit()

    def stajsil(self,bilgi):
        self.cur.execute(
            "delete from staj_mulakat where ogrenci_numara=%s,staj_baslama_tarihi=%s",  bilgi)
        self.con.commit()

    def ogrencinumaralistele(self):
        self.cur.execute("select * from ogrenci")
        result = self.cur.fetchall()
        return result
    
    def stajkurumlistele(self):
        self.cur.execute("select * from kurumlar")
        staj_kurum = self.cur.fetchall()
        return staj_kurum

    def stajkonulistele(self):
        self.cur.execute("select * from konu")
        result = self.cur.fetchall()
        return result

    def kurumekle(self,kurumadi):
        self.cur.execute("insert into kurumlar (kurum_isim) values (%s)", kurumadi)
        self.con.commit()
    
    def konuekle(self,konu_isim):
        self.cur.execute("insert into konu (konu_isim) values (%s)", konu_isim)
        self.con.commit()
   
    

    

    
    
    















    # def stajkonulistele(self):
    #     self.cur.execute("select DISTINCT (staj_konu) from staj_mulakat")
    #     result = self.cur.fetchall()
    #     return result
    
    
    