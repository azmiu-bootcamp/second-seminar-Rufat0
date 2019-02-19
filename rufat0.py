import math

def Oxu(sayi):

    birler = {"0":"","1":"Bir","2":"Iki","3":"Uc","4":"Dord","5":"Bes","6":"Alti","7":"Yeddi","8":"Sekkiz","9":"Doqquz"}
    onlar = {"1":"On","2":"Iyirmi","3":"Otuz","4":"Qirx","5":"Elli","6":"Altmis","7":"Yetmis","8":"Seksen","9":"Doksan","0":""}
    yuz = ["Yuz"]

    if len(sayi) == 3:
        if sayi[0] == "1":
            oxu = yuz[0]+onlar[sayi[1]]+birler[sayi[2]]
            return oxu
        if sayi[0] == "0":
            oxu = onlar[sayi[1]]+birler[sayi[2]]
            return oxu
        else:
            oxu = birler[sayi[0]]+yuz[0]+onlar[sayi[1]]+birler[sayi[2]]
            return oxu
    
        if  len(sayi) == 1:

           if sayi[0] == "0":
            oxu = "Sifir"
            return oxu
        
           else:
                oxu = birler[sayi[0]]
                return oxu
    if len(sayi) == 2:
        oxu = onlar[sayi[0]]+birler[sayi[1]]
        return oxu
sayi  = input("Sayiyi Giriniz :")
basaSifirYaz = len(sayi)%3
if basaSifirYaz == 1:
    sayi = "00"+sayi
    
elif basaSifirYaz == 2:
    sayi = "0"+sayi
else:
    sayi = sayi


neceYuzlerVar =  math.ceil(int(len(sayi))/3.0)

ucluGrub = {"0":"","1":"Min","2":"Milyon","3":"Milyard","4":"Trilyon","5":"Katrilyon"}

oxu = ""

for i in range(int(neceYuzlerVar)):

   if sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)] == "000":
        oxu = oxu

   elif sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)] == "001" and len(sayi) == 6:
       oxu = ucluGrub[str(i)] + oxu

   else:
       oxu = Oxu(sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)]) + ucluGrub[str(i)] + oxu


        
print (oxu)
