        #5-dars  07.06 .2022
              #Integerlar bilan ishlash
a=22
b=-28.2
c=a+b
print(int(c))
              #Floatlar bilan ishlash
kvadrat_t = 2.31
yuzasi = kvadrat_t ** 2
print(int(yuzasi))
             #Butun sondan o'nlik songa utish'
a=-20
b=40
c=b/a
print(int(c))
print(float(c))
          #Uzun sonlarni kiritish buyicha
aholi_soni = 122_222_222
print("dunyo aholisi", aholi_soni,"taga yetdi")
                    #Bir nechta uzgaruvchilarga qiymat berish
x,y,z =10,-3,33
print(x,y,z)
x= 33
y=-22
z=44
print(x)
#Uzgaruvchini turini almashtirish
#ism ='Jobir'
#yosh = 22
#xabar = ism + ' ' + yosh +'da' # matn va son kurinishidagilarni  birlashtirib bulmaydi sabab tipi har xil
#print(xabar)
               #str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
ism ='Coder'
yosh =44
xabar = ism +' ' + str(yosh) +'da'
print(xabar)
        # Uzgaruvchi turinij tekshirish
kocha ='xirmontepa'
yosh = 22
print(type(yosh))
print(type(kocha))
                #input va sonlar
                #foydalanuvchidan yoshini suraymiz va intga ugiramiz qiymatni
#tugilgan_yil =int(input("Tugilgan kuningizni kiriting:"))
#yosh =2022 - tugilgan_yil
#print("Siz"+ ' ' + str(yosh) + "ga kirdinggiz")
#print("yoshingiz" + str(yosh))
#print(type(tugilgan_yil))

        #Foydalanuvchining yoshini surang va tugilgan yilini chiqaramiz
#yosh = int(input("Yoshingiz nechida: \n>>>"))
#t_yil = 2022-yosh
#print("Siz ", t_yil, " da tug'ilgansiz")
#a=float(input("Birinchi sonni kiriting:"))
#b=float(input("Ikkinchi sonni kiriting:"))
#print(f"{a}+{b}=",int (a+b))

      #Listlar(Ruyxatlar) bilan ishlash
mevalar =["olma","anjir","banan","olcha"]
print(mevalar)
#sonlar =["12000","222222","44433434"]
#print(sonlar)
#ismlar =[] # bo'sh ruyxat
#print(ismlar)
      #Indexs bilan ishlash
mevalar =["olma","anjir","banan","olcha"]
print(mevalar[1])
print(mevalar[-2]) #oxiridan sanab boshlaydi
sonlar= ["122","233","36636"]
sonlar[0] ="Kuksi" #elementni uzgartirish
print(sonlar)
print("Birinchi meva:" + mevalar[1].title())
print("Ikkinchi meva:"+ mevalar[2].upper())
 #Elementlar ni qushish ayirish uzgartirish
mevalar [1] = "Anor" #Almashtirish
print(mevalar)
#mevalar[2] =" Kartoshka"
#print(mevalar)
#mevalar [2] =mevalar[1]+"Uzum"
#print(mevalar)
# Yangi element qushish uchun Append methoddan foydalanamiz Ruyxatning oxiriga qushadi
#.append() metodi bo'sh ro'yxatni to'ldrishda juda qulay usul. Odatda dastur boshida bo'sh ro'yxat yaratilib,
        # dastur davomida ro'yxat foydalanuvchi tomonidan to'ldirib borilishi odatiy hol.
cars=["nexia","captiva","Cobalt","Trailblazer"]
cars.append("KIA K5")
print(cars)
   #INsert methodi ruyxatni istalgan joyiga element qushadi
company =["Google", "Artel","Apple"]
company.insert(2,'Yahoo')
print(company)
       #Ruyxatdagi elemnetni index buyicha uchirish del
colors = ["Green","Yellow","Blue"]
del colors[1]
print(colors)
   # Ruyxatdagi elementni  qiymat buyicha uchirish
buildngs =["NestOne","Hilton","Greenvich"]
buildngs.remove("Hilton")
print(buildngs)
     #Elementni sug'urib olish
#street = ["Amir TEmur","Navoiy","Bog'ishmol","Beruniy"]
#mahsulot=street.pop(2)
#print("Men" + ' '+ mahsulot + " ko'chada yashayman")
korzinka =["MegaPlanet","Olcha","Archa.uz","Dachatop","Megashop"]
korzinka.sort()
print(korzinka)