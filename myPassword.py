# coding=utf-8

# md5 32 karakter
# random sayı + metinsel karakterin sayısal değeri + (Büyük/Küçük harf) / boşluk ise (_) + random sayının md5i

#TODO:: her kelimenin başında kelimenin kaç harf olduğunu ifade eden sayı değeri olacak eğer ifade eden değer kadar karakter çıkmazsa sonucu gösterme

import array
import random
import hashlib

def Sifrele(filepath):
    print("[*] Metin şifreleniyor!")
    upperChar = ["A", "B", "C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
    lowerChar = ["a", "b", "c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"," ","1","2","3","4","5","6","7","8","9","!","'","^","+","%","&","/","(",")","=","?","*","_","-","é",'"',".",",",":",";","<",">","@","~","`","´","≈","√","∫","≤","≥"]
    passLowerChar = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
    passUpperChar = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z"]

    randomNumberMd5 = hashlib.md5()
    randomNumber = random.randint(0,9)
    randomNumberMd5.update(str(randomNumber))
    randomMd5 = randomNumberMd5.hexdigest()

    cryptedText=str(randomNumber)

    f = open(filepath, "r")
    metin = f.read()

    metin = metin.decode("utf-8")
    sayac=0
    first=True
    while sayac < len(metin):
        if first==True:
            charList = [metin[sayac]]
            first=False
        else:
            charList.append(metin[sayac])
        sayac += 1

    sayac=0
    while sayac < len(charList):
        sayac2=0
        for x in lowerChar:
            sayac2+=1
            if charList[sayac].lower() == x.decode("utf-8"):
                if charList[sayac].strip() == "":
                    cryptedText+=str(sayac2-1)+"_"
                elif charList[sayac] == x.decode("utf-8"):
                    #Lower Case
                    cryptedText+=str(sayac2-1)+str(passLowerChar[random.randint(0,len(passLowerChar)-1)])
                else:
                    #Upper Case
                    cryptedText+=str(sayac2-1)+str(passUpperChar[random.randint(0,len(passUpperChar)-1)])
        sayac+=1
    f = open("sifrelenmis"+str(random.randint(0,100))+".txt", "w")
    f.write(cryptedText+randomMd5)
    f.close()
    print("[!] Şifrelenen metin, metin belgesi olarak kaydedildi!")
    # return cryptedText+randomMd5
        

def Coz(filepath):
    print("[*] Şifrelenmiş metin çözülüyor!")
    upperChar = ["A", "B", "C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
    lowerChar = ["a", "b", "c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"," ","1","2","3","4","5","6","7","8","9","!","'","^","+","%","&","/","(",")","=","?","*","_","-","é",'"',".",",",":",";","<",">","@","~","`","´","≈","√","∫","≤","≥"]

    uncryptedText=""

    sayac=0
    first=True
    f = open(filepath, "r")
    cryptedText = f.read()
    while sayac < len(cryptedText):
        if first==True:
            charList = [cryptedText[sayac]]
            first=False
        else:
            charList.append(cryptedText[sayac])
        sayac += 1

    metin=""

    #MD5 ile koruma sistemi
    randomSayi = charList[0]
    charList = charList[:0] + charList[0+1 :]
    md5=""
    silmeIndexi = (len(charList)-32)
    for i in range(32):
        md5+=str(charList[(len(charList)-32)+i])
        charList = charList[:silmeIndexi] + charList[silmeIndexi+1 :]

    randomNumberMd5 = hashlib.md5()
    randomNumber = randomSayi
    randomNumberMd5.update(str(randomNumber))
    randomMd5 = randomNumberMd5.hexdigest()

    if randomMd5 == md5:
        for x in charList:
            if x == "_":
                uncryptedText+=" "
                metin=""
            elif x.islower() == True or x.isupper() == True:
                #Metinsel ifade
                if x.lower() == x:
                    #küçük karakter
                    uncryptedText+=lowerChar[int(metin)]
                else: 
                    #büyük karakter
                    uncryptedText+=upperChar[int(metin)]
                metin=""
            elif x.islower() == False and x.isupper() == False:
                #Sayısal İfade
                metin+=str(x)
                
        f = open("cozulmus"+str(random.randint(0,100))+".txt", "w")
        f.write(uncryptedText)
        f.close()
        print("[!] Çözülen metin, metin belgesi olarak kaydedildi!")
        # return uncryptedText
    else:
        print("[!] Şifrelenmiş metin bozulmuş!")

secim = int(input("[?] İşlem Seçin 1- Şifrele | 2- Çöz : "))

if secim==1:
    Sifrele(str(raw_input("[?] Dosya Yolu: ")))
elif secim==2:
    Coz(str(raw_input("[?] Dosya: ")))



