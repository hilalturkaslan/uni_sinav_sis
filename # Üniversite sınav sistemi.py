# Üniversite sınav sistemi içerisinde dersler,vize,final ve bütünleme notları yer almaktadır. Derslerin kredisi vardır.
# Bu krediller alan ve alan dışı olarak ikiye ayrılmaktadır.



alan_bolum = ["web3, yapay zeka, sosyal medya, sistem güvenliği"]
alan_dis = ["finans, isletme"]

vize = int(input("vize notunu giriniz: "))
final = int(input("final notunu giriniz: "))
butunleme = int(input("bütünleme notunu giriniz: "))


def dersler():
    if alan_bolum.call():
        return hesapla
    if alan_dis.call():
        return hesapla
    
def sinavlar():

    if vize ==0:
        print("vizeye girmedi / 0 aldı") 

    else:
        print("vize notu hesaplandı")

    if final ==0:
        print("finale girmedi / 0 aldı")
        return butunleme
    else:
        print("final notu hesaplandı")

@sinavlar
def hesapla():
    
    hesaplama_bolum = "(vize*0.4+final*0.6)"
    if hesaplama_bolum <50:
        print("bütünlemeye giriniz")
        return butunleme
    
    else:
       print("ders başarılı")


    hesaplama_dis = "(vize*0.3+final*0.7)"
    if hesaplama_dis <60:
        print("ders tekrarı")

    else:
       print("ders başarılı")
    




