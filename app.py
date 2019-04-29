from flask import Flask,render_template,request,json,redirect,url_for
from database import Database


app = Flask(__name__)

#-----Anasayfa
@app.route("/")
def index():
    return render_template("index.html")



#----------------Öğrenci----------------

@app.route("/ogrenci")    
def ogrenci():
    db = Database() 
    result = db.ogrenci()
    return render_template("ogrenci.html",result=result)

@app.route("/dgs-ogrenci")    
def dgsogrenci():
    db = Database()
    result = db.dgsogrenci()
    return render_template("dgs-ogrenci.html",result=result)



@app.route("/ogrenci-ekle")
def  ogrenci_ekle():
    return render_template("ogrenci-ekle.html")

@app.route('/ogrenciekleme',methods = ['POST'])
def  ogrenciekleme():
   if request.method == 'POST':
      db = Database()
      ogrenci_numara = request.form['ogrenci_numara']
      ogrenci_isim = request.form['ogrenci_isim']
      ogrenci_soyisim = request.form['ogrenci_soyisim']
      ogrenci_ogretim = request.form['ogrenci_ogretim']
      staj_toplam_gun = request.form['staj_toplam_gun']
      numara = (ogrenci_numara)
      ogrenci_bilgisi = (ogrenci_numara,ogrenci_isim,ogrenci_soyisim,ogrenci_ogretim,staj_toplam_gun)
      db.numaraekle(numara)
      db.ogrenciekle(ogrenci_bilgisi)
      return redirect("ogrenci")

@app.route('/ogrencisil/<int:numara>')
def ogrencisil(numara):
    db = Database()
    db.ogrencisil(numara)
    db.numarasil(numara)
    return redirect('/ogrenci')
    

@app.route("/dgs-ogrenci-ekle")
def  dgs_ogrenci_ekle():
    return render_template("dgs-ogrenci-ekle.html")


@app.route('/dgsogrenciekleme',methods = ['POST'])
def  dgsogrenciekleme():
   if request.method == 'POST':
      db = Database()
      ogrenci_numara = request.form['ogrenci_numara']
      ogrenci_isim = request.form['ogrenci_isim']
      ogrenci_soyisim = request.form['ogrenci_soyisim']
      ogrenci_ogretim = request.form['ogrenci_ogretim']
      staj_toplam_gun = request.form['staj_toplam_gun']
      onceki_okul = request.form['onceki_okul']
      numara = (ogrenci_numara)
      oncekistaj=int(staj_toplam_gun) / 2
      
      ogrenci_bilgisi = (ogrenci_numara,ogrenci_isim,ogrenci_soyisim,ogrenci_ogretim,oncekistaj,onceki_okul)
      db.numaraekle(numara)
      db.dgsogrenciekle(ogrenci_bilgisi)
      return redirect("dgs-ogrenci")

@app.route('/dgsogrencisil/<int:numara>')
def dgsogrencisil(numara):
    db = Database()
    db.dgsogrencisil(numara)
    db.numarasil(numara)
    return redirect('/dgs-ogrenci')
 

@app.route('/dgsogrencibilgileri/<int:numara>')
def dgsogrencibilgileri(numara):
    db = Database()
    sonuc = db.dgsogrencilistele(numara)
    normalstaj = db.ogrencilistele(numara)
    stajlar = db.dgsogrencistajlistele(numara)
    return render_template("dgs-ogrenci-duzenle.html",sonuc=sonuc,stajlar=stajlar,normalstaj=normalstaj)


@app.route("/dgsogrenciduzenle")    
def dgsogrenciduzenle():
    return render_template("dgs-ogrenci-duzenle.html")   

@app.route("/dgsogrenciduzenleme/",methods=['POST'])
def dgsogrenciduzenleme():
    if request.method == 'POST':
      db = Database()
      ogrenci_numara = request.form['ogrenci_numara']
      ogrenci_isim = request.form['ogrenci_isim']
      ogrenci_soyisim = request.form['ogrenci_soyisim']
      ogrenci_ogretim = request.form['ogrenci_ogretim']
      onceki_okul = request.form['onceki_okul']
      
      
      ogrenci_bilgisi = (ogrenci_isim,ogrenci_soyisim,ogrenci_ogretim,onceki_okul,ogrenci_numara)
      db.ogrenciduzenle(ogrenci_bilgisi)

    return redirect("dgs-ogrenci")



@app.route('/ogrencibilgileri/<int:numara>')
def ogrencibilgileri(numara):
    db = Database()
    sonuc = db.ogrencilistele(numara)
    stajlar= db.ogrencistajlistele(numara)
    
    return render_template("ogrenciduzenle.html",sonuc=sonuc,stajlar=stajlar)

@app.route("/ogrenciduzenle")    
def ogrenciduzenle():
    return render_template("ogrenciduzenle.html")   

@app.route("/ogrenciduzenleme",methods=['POST'])
def ogrenciduzenleme():
    if request.method == 'POST':
      db = Database()
      ogrenci_numara = request.form['ogrenci_numara']
      ogrenci_isim = request.form['ogrenci_isim']
      ogrenci_soyisim = request.form['ogrenci_soyisim']
      ogrenci_ogretim = request.form['ogrenci_ogretim']
      staj_toplam_gun = request.form['staj_toplam_gun']
      ogrenci_bilgisi = (ogrenci_isim,ogrenci_soyisim,ogrenci_ogretim,staj_toplam_gun,ogrenci_numara)
      db.ogrenciduzenle(ogrenci_bilgisi)

    return redirect("ogrenci")


# --------------------------------Komisyon--------------------------------------

@app.route("/komisyon")
def komisyon():
     db = Database() 
     result = db.akademisyen()
     return render_template("komisyon.html",result=result)

@app.route("/komisyon-ekle")
def komisyon_ekle():
     return render_template("komisyon-ekle.html")

@app.route('/komisyonekleme',methods = ['POST'])
def komisyonekleme():
   if request.method == 'POST':
      db = Database()
      komisyon_numara = request.form['komisyon_numara']
      komisyon_isim = request.form['komisyon_isim']
      komisyon_soyisim = request.form['komisyon_soyisim']
      komisyon_unvan = request.form['komisyon_unvan']
      akademisyen_bilgisi = (komisyon_numara,komisyon_isim,komisyon_soyisim,komisyon_unvan)
      db.akademisyenekle(akademisyen_bilgisi)
      return redirect("komisyon")


@app.route('/komisyonbilgileri/<int:numara>')
def komisyonbilgileri(numara):
    db = Database()
    sonuc = db.komisyonlistele(numara)
    return render_template("komisyonduzenle.html",sonuc=sonuc)

@app.route("/komisyonduzenle")    
def komisyonduzenle():
    return render_template("komisyonduzenle.html")   

@app.route("/komisyonduzenleme",methods=['POST'])
def komisyonduzenleme():
    if request.method == 'POST':
      db = Database()
      komisyon_numara = request.form['komisyon_numara']
      komisyon_isim = request.form['komisyon_isim']
      komisyon_soyisim = request.form['komisyon_soyisim']
      komisyon_unvan = request.form['komisyon_unvan']
      komisyon_bilgisi = (komisyon_isim,komisyon_soyisim,komisyon_unvan,komisyon_numara)
      db.komisyonduzenle(komisyon_bilgisi)

    return redirect("komisyon")


@app.route('/komisyonsil/<int:numara>')
def komisyonsil(numara):
    db = Database()
    db.komisyonsil(numara)
    return redirect('/komisyon')

#------------------------------------Staj---------------------------------------

@app.route("/staj")
def staj():
     db = Database()
     result = db.staj()
     return render_template("staj.html",result=result)

@app.route("/staj-ekle")
def staj_ekle():
     db = Database() 
     result = db.ogrenci()
     komisyon = db.akademisyen()
     staj_kurum = db.stajkurumlistele()
     staj_konu = db.stajkonulistele()
     dgs_ogrenci = db.dgsogrenci()
     return render_template("staj-ekle.html",result=result,komisyon=komisyon,staj_kurum=staj_kurum,dgs_ogrenci=dgs_ogrenci,staj_konu=staj_konu)

@app.route('/stajsil/<int:numara>/<string:baslangic>')
def stajsil(numara,baslangic):
    db = Database()
    data=(numara, baslangic)
    db.stajsil(data)
    return redirect('/dgs-ogrenci')



@app.route("/kurumekleme", methods = ['POST'])
def kurum_ekle():
     db = Database() 

     if request.method == 'POST':
          kurum_adi = request.form['kurum_adi']
          db.kurumekle(kurum_adi)
     return redirect("/staj-ekle")
     

@app.route("/konuekleme", methods = ['POST'])
def konu_ekle():
     db = Database() 

     if request.method == 'POST':
          konu_isim = request.form['konu_isim']
          db.konuekle(konu_isim)
     return redirect("/staj-ekle")


@app.route('/stajekleme', methods=['GET', 'POST'])
def stajekleme():
    db = Database()

    if request.method == 'POST':
        ogrenci_numara = request.form['ogrenci_numara']
        staj_baslama_tarihi = request.form['staj_baslama_tarihi']
        staj_bitis_tarihi = request.form['staj_bitis_tarihi']
        staj_kurum = request.form['staj_kurum']
        staj_sehir = request.form['staj_sehir']
        staj_konu = request.form['staj_konu']
        staj_toplam_gun = request.form['staj_toplam_gun']
        mulakat_kontrol = request.form['mulakat_kontrol']
        staj_sinif = request.form['staj_sinif']
        mulakat_tarih = request.form['mulakat_tarih']
        mulakat_saat = request.form['mulakat_saat']
        komisyon_uye_1 = request.form['komisyon_uye_1']
        komisyon_uye_2 = request.form['komisyon_uye_2']
        devam = request.form['devam']
        caba_ve_calisma = request.form['caba_ve_calisma']
        amire_karsi_davranis = request.form['amire_karsi_davranis']
        is_arkadasina_karsi_davranis = request.form['is_arkadasina_karsi_davranis']
        isi_vaktinde_yapma = request.form['isi_vaktinde_yapma']
        proje = request.form['proje']
        duzen = request.form['duzen']
        sunum = request.form['sunum']
        icerik = request.form['icerik']
        mulakat = request.form['mulakat']
        staj_kabul_edilen_gun = request.form['staj_kabul_edilen_gun']
        if (int(staj_sinif == 2) and int(staj_toplam_gun) > 25) :
             hata = "2. Sınıf Öğrencisi Maksimum 25 Gün Staj Yapabilir."
             return render_template("staj.html",hata=hata)
        if  (int(staj_toplam_gun) < 15) :
             hata = "15 günden az staj Yapılamaz"
             return render_template("staj.html",hata=hata)
        else:                                                                                     
          data = (ogrenci_numara, staj_baslama_tarihi, staj_bitis_tarihi,staj_sehir,staj_konu,staj_kurum,staj_toplam_gun,staj_sinif,staj_kabul_edilen_gun,mulakat_kontrol,mulakat_tarih,mulakat_saat,komisyon_uye_1,komisyon_uye_2,devam,caba_ve_calisma,isi_vaktinde_yapma,amire_karsi_davranis,is_arkadasina_karsi_davranis,proje,duzen,sunum,icerik,mulakat)
          db.stajekle(data)
        

    
    return redirect('/staj')



@app.route("/ayarlar")
def ayarlar():
     
     return render_template("ayarlar.html")


if __name__ == "__main__":
   app.run(debug = True)


   