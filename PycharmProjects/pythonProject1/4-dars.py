
#name ='Khikmat'
#print(name)
#x=22;
#y=21;
#c=x+y
#print(c)
#print(' "Men CoreI5" komputerni tuzatmoqchiman')
#matnimizni pastgi qatorga tushirish uchun \n bilan matnni ikkiga bulamiz yani pastga qatorga tushiramiz
#print("""Odami ersang,demagil odami\n Oniki,yo'q xalq g'amidin g'ami""")
#print('Odami ersang, demagil odammi  Oniki,yo\'q xalq g\'amidin g\'ami')  bir tirnoqdan foydalanib ham  chiqarsak buladi natijani
#5 ning 4 darajais
#print(5**4)
#print("Kaetlari 3 va4 bulgan tugri burchakli ucburcakning  gipotenuzasi:",float((3**2+4**2)**(1/2)))

#      Uzgaruvchilar  mavzusi
#ism = "Khikmat"
#yosh = 23
#print(ism)
#print(yosh)
#ism = "Abduloloh"
#print(ism)
#yosh = 32
#print(yosh)
          #2-masala
radiusi = 5
pi =3.14159
aylana_yuzi = pi*radiusi**2
print("Radiusi",radiusi,"ga teng aylananing yuzi=", aylana_yuzi)
        #3-masala
# kubning hajmini va yoqlarining yuzining topish formulasi
radiusi=3
hajmi = radiusi**3
print("Kubning","hajmi=",hajmi,"ga teng")
      #29.06 2022
      #String methodlari bilan ishlash
#Matnlarni qo'shish operatori
ism = 'Hikmat'
print("Mening ismim " + ism)

#coder = '23'
#ism ='Abdulvosid'
#print("Menig yoshim " + coder + "da")
  # Orasiga bushliq quyish uchun '' dan foydalanamiz
ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' +  familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz
#         Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish
#          uchun f-string usulidan  f"{matn1} {matn2}" ham foydalanamiz:
ism = "Ne'mat"
familiya = 'Teshaboyev'
sharifi =   f"{ism} {familiya}"
print(sharifi)
ism = "Abdumalik"
familiya = 'Abdujalilov'
print(f"Salom, mening familiyam {familiya}. {ism} {familiya}!")

 #Matnga bushliq quyish uchun  maxsus belgilar va f stringdan foydalandik
yosh = '24'
familiya = 'Ahadov'
ism = 'Sherzod'
ism_sharifi = f"{ism} {familiya}" +"\tMansurovich"
print(ism_sharifi)
# Upper va Lower and Title va capatalize methodlari
familiya = 'Ahadov'
ism = 'Sherzod'
ism_sharifi = f"{ism} {familiya}" + "\tMansurovich"
print(ism_sharifi.upper())
print(ism_sharifi.lower())
print(ism_sharifi.title()) # titleni vazifasi har bir suzning 1-harfini bosh harfa katta harfda chiqaradi
print(ism_sharifi.capitalize()) # 1-so'zni bosh harfda chiqaradi

#   strip,rstrip,lstrip methodlari
viloyat = '        Toshkent shahri           '
#print("Men" + viloyat+"da"+ "\tyashayman")
print(" Men " +viloyat.strip()+"da" + "\tyashayman")
print("Men" + viloyat.rstrip()+"da" +"dasturchi bulib ishlayman")
print("Men" +viloyat.lstrip() +"da" +"ishlayman")






          #Inputlar bilan ishlash
#ism = input("Isminggizni kiriting:")
#print("assalomu  aleykum" + ' '+ ism)
#print("assalomu  aleykum" +' '+ ism.title())
#print("Men dasturchi bulmoqchiman" + ' ' + ism.lower())
#kocha = 'Amir temur'
#mahalla = 'Shoh 119'
#viloyat = 'Toshkent'
#tuman = 'Yunusobod'
#print(f"{kocha},{mahalla},{tuman},{viloyat}")

kocha = input("Kochani nomini kiriting:")
mahalla = input('Mahallanggiz:')
tuman = input('Tuman:')
shahar = input('Shahringgiz:')
print("mening kucham" +kocha)
#print( "Mening ko'cham:"f"{kocha}   \nMahalla:{mahalla}   \nTuman:{tuman}  \nShahar:{viloyat}")




