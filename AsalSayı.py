Sayı1 = int(input ('Birinci sayıyı girin:')) 
Sayı2 = int(input ('İkinci sayıyı girin:')) 
Sayı3 = int(input ('Üçüncü sayıyı girin:')) 
Sayı4 = int(input ('Dördüncü sayıyı girin:')) 
Sayı5 = int(input ('Beşinci sayıyı girin:')) 
GirilenSayı1 = [Sayı1]
GirilenSayı2 = [Sayı2]
GirilenSayı3 = [Sayı3]
GirilenSayı4 = [Sayı4]
GirilenSayı5 = [Sayı5]

print ('Girilen sayılar sırası ile: {0}, {1}, {2}, {3}, {4}'.format(Sayı1, Sayı2, Sayı3, Sayı4, Sayı5))
for Sayı1 in GirilenSayı1 :
    for a in range(2,Sayı1):
        if (Sayı1 % a) == 0: 
            print('Birinci sayı asal değildir.({0})'.format(Sayı1))
            break
        else: 
            print('Birinci sayı asaldır.({0})'.format(Sayı1))        
            break
for Sayı2 in GirilenSayı2 :
    for b in range(2,Sayı2):
        if (Sayı2 % b) == 0: 
            print ('İkinci sayı asal değildir.({0})'.format(Sayı2)) 
            break
        else: 
            print('İkinci sayı asaldır.({0})'.format(Sayı2))
            break
for Sayı3 in GirilenSayı3 :
    for c in range(2,Sayı3):
        if (Sayı3 % c) == 0: 
            print ('Üçüncü sayı asal değildir.({0})'.format(Sayı3))
            break
        else: 
            print('Üçüncü sayı asaldır.({0})'.format(Sayı3)) 
            break
for Sayı4 in GirilenSayı4 :
    for d in range(2,Sayı4):
        if (Sayı4 % d) == 0: 
            print ('Dördüncü sayı asal değildir.({0})'.format(Sayı4))
            break
        else: 
            print('Dördüncü sayı asaldır.({0})'.format(Sayı4))
            break
for Sayı5 in GirilenSayı5 :
    for e in range(2,Sayı5):
        if (Sayı5 % e) == 0: 
            print ('Beşinci sayı asal değildir.({0})'.format(Sayı5))
            break
        else: 
            print('Beşinci sayı asaldır.({0})'.format(Sayı5))
            break