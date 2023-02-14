
    #Ruyxatlar bilan ishlash
# books = ["Alvido","Ezgu tilaklar","Shaxmat doskasi","Mehrobdan chayon"]
# books.sort()
# print(books)
# Tartiblashda katta harflar kichik harflardan avval kelishini hisobga oling.
    # Agar matndagi so'zlarning bosh harfi katta-kichik aralash yozilgan bo'lsa,
    # ularni bir ko'rinishga keltirib olish maqsadga muvofiq bo'ladi.
# articles = ["paper","books","hidoyat","Al-Buxoriy"]
# articles.sort()
# print(articles)
#Ro'yxatni teskari saqlash uchun reverse=True argumentidan foydalanamiz
# guess = ['Avazbek',"Hasan","Husanboy","Shirinaxon"]
# guess.sort(reverse=True)
# print(guess)
   # Ruyxatni aylantirish  uchun .reverse methodidan foydalanamiz.

# fruits = ["Banan","Olcha","Gilos","Apelsin"]
# fruits.reverse()
# print((fruits))
#Ruyxatni uzunligini aniqlash uchun len funksiyasidan foydalanamiz
# cars=["BMW","Matiz","Cobalt","TRailblazer"]
# print(len(cars))

 #Range funksiyasi malum bir oraliqqa sonlar ketma ketligini hosil qilamiz.
# sonlar = list(range(1,10+1))
# print(sonlar)
# juftsonlar =list(range(1,15+1,2))
# print(juftsonlar)

                  # SONLI RO'YXAT USTIDA SODDA AMALLAR
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
                    #Ruyxatni kesish
# cars=["bmw","captiva","Lasetti","spark"]
# my_blog = cars[0:3]
# print(my_blog)
                    # Ruyxatdan nusxa olish
# sonlar = [1,2,3,4,5,6,7]
# son[1]
# print(sonlar2)
                   # TUPLES - O'ZGARMAS RO'YXAT Qiymatlar bir marta beriladiuzgartirib ham bo'lmaydi

# toys = ("bus","car","dino","snake") #o'zgarmas ruyxat ()
# toys =list(toys)
# toys.insert(2,"fish")
# print(toys)
   #O"zgarmas ruyxatni oddiy ruyxatga uykazish
# bills = ("bus","car","dino","snake")
# bills=list(bills)
# bills.insert(1,"mouse")
# print(bills)



#Butun son berilgan. Agar u musbat bo‘lsa unga 1 qo‘shilsin, aks holda o‘zgarishsiz qoldirilsin.
   # Olingan son chiqarilsin.
# a=int(input("a sonini kiriting:"))
# if a>0 :
#     print(a+1)
# else:
#     print(a)
a=int(input(" a="))
b=int(input(" b="))
if a>b :
    print(a)
else:
    print(b)