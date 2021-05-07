Türkçe_harfler = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']

def HarfFiltresi(Türkçe_harfler):

    ilk_string ="Ah5me4t"
    x = ilk_string.lower()
    if (Türkçe_harfler in x):
        return True
    else :
        return False
HarfleriFiltrele = filter (HarfFiltresi,Türkçe_harfler)
for İlkİsimHarfler in HarfleriFiltrele :
    print (İlkİsimHarfler,end = "")