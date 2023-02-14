#for uchun ketma ketlik yetarli
#While xuddi shunday bir xil vazifani bajaradi forga uxshaydi
#while shart=true loop buladi >>> False loop sikl tuxtaydi
# a=5
# while a>1:
#     print("Salom")
#     break
#     #if a<=4:
#        #continue
#     a -= 1 # Tuxtash sharti, break funksiyasi
#  ##   false qiymat qaytargancha tuxtash
#  1-masala  a va b musbat sonlar berilgan(a>b). a uzunlikdagi kesmaga b uzunlikdagi kesmani mumkin
#qadar eng ko‘p miqdorda joylashtirilganda, a kesmaning bo‘sh (ortib) qolgan bo‘lagi topilsin.
#Ko‘paytirish va bo‘lish operatsiyalaridan foydalanilmasin.
# a=int(input("a = "))
# b=int(input("b = "))
# while a>b:
#     a-=b #shartni tuxtadigan jarayon
# print(a)
# 2. a va b musbat son berilgan(a>b). a uzunlikdagi kesmaga b uzunlikdagi kesma mumkin qadar
# eng ko‘p miqdorda joylashtirilgan bo`lsa, (Ko‘paytirish va bo‘lish operatsiyalaridan foydalanmay)
# a kesmaga joylashtirilgan b kesmalar soni aniqlansin.
# a=int(input(" a= "))
# b=int(input(" b= "))
# sanoq = 0
# while a>b:
#     a-=b
#     sanoq += 1
# print(a)
# print(sanoq)



# 3-masala 3. n va k musbat butun sonlari berilgan. Faqat qo‘shish va ayirish operatsiyasidan foydalanib n ni
# k ga bo‘lganda bo‘linmaning butun hamda qoldiq qismi topilsin.
# n=int(input("n = "))
# k=int(input( "k = "))
# bulinma=0
# while n>k:
#     n-=k
#     bulinma +=1
# print(bulinma)
# print(n)

#  4-masala n(n>0) butun son berilgan. Agar u 3 sonining darajasidan iborat bo‘lsa true, aks holda false
# chiqarilsin.
# n = int(input("n = "))
# k=1
# while n>3**k:
#     k += 1
#     #print(3**k)
# if 3** k == n:
#      print(True)
# else:
#     print(False)




#
#  5-masala n(n>0) butun son berilgan. U 2 ning biror bir darajasidan iborat bo‘lsa n=2k, shu darajaning
# ko‘rsatkichi k butun soni topilsin.
#1024  >> 10
# k=1
# n=int(input('n=  '))
# while  2**k<n:
#     k += 1
#     #print(2**k, end=' ')
# if 2 ** k==n:
#      print(k)
# else:
#     print(" 2 ni darajasi emas")

#
# 6-masala n(n>0) butun son berilgan. n ikki factorial hisoblansin. Bu yerda n!!=n(n-2)(n-4)… (oxirgi
# ko‘paytuvchi agar n-juft bo‘lsa 2 ga, toq bo‘lsa 1 ga teng.) Butun tip diapozonidan oshib
# ketishining oldini olish uchun bu ko‘paytma natija haqiqiy tipli o‘zgaruvchiga qiymatlanadi.
# n!!=n*(n-2)(n-4)
# 6!!=6*4*2
# 7!!=7*5*3*1
# fact2=1
# n=int(input('n='))
# while n>=1:
#     print(n,end= "*")
#     fact2*=n
#     n-=2
# print(fact2)

#  7-masala n(n>0) butun son berilgan. Kvadratdan ildiz chiqarish formulasidan foydalanmay kvadrati n
# dan katta eng kichik k soni topilsin. (k2>n)
# n=int(input("n = "))
# k=1
# while k**2<=n:
#     k+=1
#    # print(k**2,n)
# print(k)

# 8. n butun son berilgan. Kvadratdan ildiz chiqarish formulasidan foydalanmay kvadrati n dan katta
# bo‘lmagan eng katta butun k soni topilsin. (k2≤n)
# n = int(input("n = "))
# k=1
# while k**2<=n:
#     k+=1
#     print(k**2,n,end=" ")
# print(k)
# # 9. n(n>1) butun son berilgan. 3k>n tengsizlik o‘rinli bo‘ladigan eng kichik k butun soni topilsin.
# n= int(input("n = "))
# k=1
# while n>3**k:
#     k+=1
#     print(3**k)
# print(" k ning qiymati=",k)
#


# 10. n(n>1) butun son berilgan. 3k<n tengsizlik o‘rinli bo‘ladigan eng katta k butun soni topilsin.
# n= int(input("n = "))
# k=1
# while n>3**k:
#     k+=1
#     print(3**k)
# print("k ning qiymati = ",k)



# 11. n(n>1) butun son berilgan. 1+2+…+k yig‘indining n dan katta yoki teng bo‘lishini
# ta`minlaydigan eng kichik k butun soni va yig‘indining qiymati chiqarilsin. (1+2+…+k≥n)
#
# n=int(input("n = "))
# summa=0
# k=1
# while summa<=n:
#     k +=1
#     summa+=k
# print( " k ning qiymati= ",k-1,summa)


# 12. n(n>1) butun son berilgan. 1+2+…+k yig‘indining n dan kichik yoki teng bo‘lishini
# ta’minlaydigan eng katta k butun son va yig‘indining qiymati chiqarilsin. (1+2+…+k≤n)
# 10 >>> 1+2+3+4<=10

# n=int(input("n= "))
# summa=0
# k=0
# while summa<=n:
#     k += 1
#     summa +=k
#
# print(k-1,summa-k)




# 13. a(a>1) son berilgan. k
# 1
# ...
# 2
# 1
# 1  
# yig‘indining a dan katta bo‘lishini ta`minlaydigan eng
# kichik k butun son va yig‘indining qiymati chiqarilsin.
# 
# 
# 
# 
#     a
# k
# 1
# ...
# 2

# a=float(input("a = "))
# summa=0
# k=0
# while summa<a:
#     k+=1
#     summa+=k**(-1)
#
# print(k+1,summa+k**(-1))
#

# 14. a(a>1) son berilgan. k
# 1
# ...
# 2
# 1
# 1  
# yig‘indi a dan kichik bo‘ladigan eng katta k butun son va
# yig‘indi chiqarilsin.

# a=float(input("a="))
# summa=0
# k=0
# while summa<a:
#     k+=1
#     summa+=k**(-1)
#
# print(k+1,summa+k)
#
# 15. Bankdagi boshlang‘ich qo‘yilma summa 1000 so‘m bo‘lsa va u har oyda p foiz ko‘payib borsa (p-haqiqiy son, 0<p<25)
# necha oydan so‘ng qo‘yilma 1100 so‘mdan oshishi(o‘tgan oylar soni) k, hamda qo‘yilmaning oxirgi miqdori s(haqiqiy son) chop etilsin.
p=float(input("p ="))
k=1
s=1000
summa=0
while 0<p<25:
    k+=1
    summa+=(s*p)/100
    if summa>1100:
        print(k)
    else:
        print(" hech qanday ")


























