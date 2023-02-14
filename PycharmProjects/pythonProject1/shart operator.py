#1. Butun son berilgan. Agar u musbat bo‘lsa unga 1 qo‘shilsin, aks holda o‘zgarishsiz qoldirilsin. Olingan son chiqarilsin.
# a=int(input("a sonini kiriting:"))
# if a>0 :
#     print(a+1)
# else :
#     print(a)
#Butun son berilgan. Agar u manfiy bo‘lsa unga 1 qo‘shilsin, aks holda 2 ayirib tashlansin. Olingan son chiqarilsin.

# a=int(input("a sonini kiriting:"))
# if a<0 :
#     print(a+1)
# else:
#     print(a-2)

 #4. Uchta butun son berilgan. Ular orasidan musbatlari soni topilsin. CHala
# a=int(input("a sonini kiriting"))
# b=int(input("b sonini kiriting"))
# c=int(input("c sonini kiriting"))
# d=3
# if a,b,c>0 :
#     print("musbat sonlar")

# 6. Ikkita son berilgan. Ulardan kattasi chiqarilsin.
# a=int(input("a sonini kiriting"))
# b=int(input("b sonini kiriting"))
# if a>b :
#     print(a)
# else:
#     print(b)

# Ikkita son berilgan. Ulardan kichigining tartib raqami chiqarilsin.
# a=int(input("a sonini kiriting:"))
# b=int(input("b sonini kiriting:"))
# if b>a :
#     print(1)
# else:
#     print(2)


# 8. Ikkita son berilgan. Ulardan dastlab kattasi so‘ngra kichigi navbat bilan chiqarilsin.
# a=int(input("a sonini kiriting:"))
# b=int(input("b sonini kiriting:"))
# if a>b :
#     print(a)
# else:


#26 masala
# x=int(input("x ni kirting:"))
# if x<=0 :
#     y=-x
# elif 0<x<2 :
#     y=x**2
# else:
#     y=4

# print(y)
# 9 Ikkita haqiqiy turga tegishli a va b o‘zgaruvchilari berilgan. Ularning qiymatlari quyidagicha qayta taqsimlansin:
# a ga kichigi b ga kattasi, a va b larning yangi qiymatlari chiqarilsin.
# a=float(input("a sonini kiriting:"))
# b=float(input("b sonini kiriting:"))
# if a>b:
#     a,b = b,a
#     print(a,b)
# #27-masala:
# x=float(input("x= "))
# if x<0 and x>4 :
#  y=0
# elif 0<=x<1 and 2<=x<3 :
#     y=1
# else:
#     y=-1
# print(y)
#28. Yil nomeri berilgan. Bu yildagi kunlar soni aniqlansin(ma’lumki kabisa bo‘lmagan yil 365
#kundan, kabisa yili 366 kundan iborat).
 # 4 yilda bir keladi 2004
yil=int(input("yilni kiriting:"))
if yil % 400 == 0 or (yil%4 ==0 and yil%100!=0) :
    print("366")
else:
    print("365")