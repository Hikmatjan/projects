#1. k va n (n>0) butun sonlar berilgan. n marta k soni chiqarilsin.
 # range 3 xil qiymat qabul qiladi Stop step,
# k=int(input("k sonini kiriting:"))
# n=int(input("n sonini kiriting:"))
# for i in range(n):
#     print(k,end=' ')
#  2. a va b butun sonlar berilgan(a>b). a va b sonlari orasidagi sonlarni o‘sish tartibida chiqarilsin(a
# va b sonlari ham kiradi) hamda shu sonlar miqdori (soni) n chiqarilsin.
# a=int(input("a="))
# b=int(input("b="))
# for i in range(a,b+1):
#    print(i)
#3. a va b butun sonlar berilgan(a<b). a va b sonlari orasidagi sonlarni kamayish tartibida
#chiqarilsin(a va b sonlari ham kiradi) hamda shu sonlar miqdori (soni) n chiqarilsin.
# a=int(input("a="))
# b=int(input("b="))
# for i in range(a,b,-1):
#     print(i)

# range 3 xil qiymat qabul qiladi:start step stop
# for i in range(222,100+1,-5):
#     print(i)

# for i in range(100):
#     if i==4:
#         continue
#     print("hello")


# pass
# for i in range(100):
#     pass


#4. 1 kg konfetning narxi haqiqiy sonda berilgan. 1,2,…, 10 kg konfetning bahosi chiqarilsin.
# narx=float(input("1 kg konfetni narxini kiriting:"))
# for i in range(1,11):
#     print(int(i*narx )," ", end="")

# 5. 1 kg konfetning narxi berilgan. 0,1, 0,2, …, 1 kg konfetning bahosi chiqarilsin.
# narx=int(input("1 kg konfetni narxini kiriting:"))
# for i in range(1,11):
#     print((i*narx/10),end=" ")


# 6. 1 kg konfetning narxi berilgan. 1,2, 1,4, …, 2 kg konfetning bahosi chiqarilsin.
# narx =int(input("1 kg konfetni narxi:"))
# for i in range(12,22,2):
#     print(int(i*narx/10),end=" ")


#7. 2 ta a va b butun sonlar berilgan. (a<b) a dan b gacha bo‘lgan butun sonlar yig‘indisi topilsin.
# a=int(input("a="))
# b=int(input("b="))
# summa=0
# for i in range(a,b+1):
#     summa+=i
# print(summa)


#8. 2 ta a va b butun sonlar berilgan. (a<b) a dan b gacha bo‘lgan sonlarning
# ko‘paytmasi topilsin
# a=int(input("a="))
# b=int(input("b="))
# if a<b :
#     summa=1
#     for i in range(a,b+1):
#         summa*=i
#     print(summa,end=" ")
# else:
#     print("a soni kichik")


#9. a va b butun sonlar berilgan. (a<b) a dan b gacha bo‘lgan sonlarning kvadratlar yig‘indisi
#topilsin.
# a=int(input("a="))
# b=int(input("b="))
# if a<b:
#     summa=0
#     for i in range(a,b+1):
#         summa+=i*i
#     print(summa,end=" ")
# else:
#     print("a soni kichik")


#10. n(n>0) butun soni berilgan Yig‘indi hisoblansin.
# n=int(input("n="))
# if n>0:
#     summa=0
#     for i in range(1,n+1):
#         summa+= 1/i
#     print(summa,end=" ")
# else:
#     print("manfiy son" )



# 11 n butun soni berilgan n3+(n+1)3+(n+2)3…+(2n)3.
# (Yig‘indi butun son). Yig‘indi hisoblansin.
# n=int(input("n="))
# summa=0
# for i in range(n,2*n+1):
#              summa+=i**3
# print(summa)



#12. n butun soni berilgan 1,11,21.3 ...1,n(n ta ko‘paytuvchi). Ko‘paytma hisoblansin
# n=int(input("n="))
# # summa=1
# # for i in range(1,n+1):
# #     summa*=1+i/10
# # print(summa)


#n(n>0) butun soni berilgan. 1,1-1,2+1,3-… Ifodaning qiymati topilsin. Shart operatori
#qo‘llanilmasin.
# n=int(input("n="))
# summa=1
# for i in range(11,11+n):
#     summa += -(-1) ** i * i / 10
# print(summa)


#14 n(n>0) butun soni berilgan. Quyidagi formuladan foydalanib berilgan sonning kvadrati
#hisoblansin: n2=1+3+5+…+(2n-1). Har bir qadamdagi yig‘indi chiqarilsin(natijada 1 dan n gacha
#bo‘lgan butun sonlarning kvadrati chiqadi). Do not understand
# n=int(input("n="))
# summa=1
# for i in range(1,2*n-1,2):
#     print(i)
#     summa+=i**2


#15. a haqiqiy va n butun sonlari berilgan(n>0). a a a ... a. n     (a, n marta ko‘paytirilgan) a ning
#n- darajasi hisoblansin. DO not understand
# a=float(input("a="))
# n=int(input("n="))
# summa=1
# if a>0:
#     print("Musbat son")
#     for i in "n":
#         summa= i**2
#     print(summa)
# else:
#     print("manfiy son")


# 16. a va n sonlari berilgan. Bitta sikldan foydalanib a sonining 1 dan n gacha bo‘lgan darajalari
# chiqarilsin.
# 2,3 natija 2,4,8 chiqsin
# a=int(input("a="))
# n=int(input("n="))
# for i in range(1,n+1):
#     print(a**i)


# 17-masala
# a=int(input("a="))
# n=int(input("n="))
# summa=1
# for i in range(1,n+1):
#     summa+=a**i
#     print(a**i)
# print(summa)


#18. a va n sonlari berilgan.1-a+a2-a3+…+(-1)nan. Bitta sikldan foydalanib ifodaning qiymati
# #hisoblansin. Hisoblashda shart operatoridan foydalanilmasin.  Do not understand
# a=int(input("a="))
# n=int(input("n="))
# summa=0
# for i in range(1,n+1):
#     summa+=-(-1)**(i+1)+a
#
# print(summa)
#19. n(n>0) butun son berilgan. n!12... n (n-faktorial) ko‘paytma hisoblansin. Ifodaning
#natijasi butun sonlar diapazonidan chiqib ketishi mumkinligi hisobga olinib, natijani saqlash uchun
#haqiqiy tipli o‘zgaruvchidan foydalanilsin va natija ham haqiqiy son ko`rinishida chiqarilsin.
# n=int(input("n="))
# summa=1
# for i in range(1,n+1):
#     summa*= i
# print(f"{n}! = ", summa)






#33. n (n>1) butun son berilgan. Butun tipli fk fibonachchi sonlar ketma-ketligi quyidagicha
#aniqlanadi. f1=1; f2=1; fk=fk-2+fk-1,k=3,4,..f1, f2,…,fn elementlari chiqarilsin.

#1, 1, 2, 3, 5, 8, 13, 21.....
#n -->> 1, 1, 2, 3, 8,
# n =int(input('n= '))
# f1=1
# f2=1
# print(f1, f2, end=' ')
# for i in range(3,n+1):12

#     fi=f2+f1
#     f1,f2=f2,fi
#     print(fi,end=' ')
   #27 -masala
# x=float(input("x="))
# n=int(input("n="))
# summa=0
# maxraj=1
# surat=1
# for i in range(1,n+1):
#    surat*=(2*i-1)
#    maxraj*=(2*i)
#    summa+=surat*x**(2*i-1)/(maxraj*(2*i-1))
# print(summa)
   #30-masala
# for ga oid misol
# n = int(input('n = '))
# from math import sin
# a=float(input('a = '))
# b=float(input('b = '))
# h = (b-a)/n
# print("h =",h)
# x = a
# for i in range(n):
#    print(1-sin(x))
#    x +=h
# print(1-sin(b))
#35-masala

#n (n>3) butun son berilgan. ak butun sonli ketma-ketlik quyidagicha aniqlanadi. a1=1; a2=2;
# a3=3 ak=ak-1+ak-2-2ak-3, k=4,5,...a1, a2, …, an elementlari chiqarilsin.
# a3=1
# a2=2
# a1=3
# n=int(input("n = "))
# print(a3,a2,a1,end=' ')
# for i in range(4,n+1):
#    ai = a1+a2-2*a3
#    a1,a2,a3=ai,a1,a2
#    print(ai,end=' ')





















