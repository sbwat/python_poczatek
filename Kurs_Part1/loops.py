#WHILE

    #Zad1
# i=0
# liczba=int(input("Podaj liczbę parzystą:"))
#
# while liczba % 2 != 0 and i < 9:
#     liczba=int(input("Podana liczba nie jest parzysta, spróbuj ponownie: "))
#     if i>=8:
#         print("Skonczył Ci się czas :P")
#     i+=1
#
# if (liczba % 2) == 0:
#     print("Dobra robota")

#     #Zad2
# phone_nb=input("Podaj numer telefonu: ").replace("-","")
# i=0
#
# new_nb=""
# print(len(phone_nb))
# while i<len(phone_nb):
#     if i %3 == 0 and i !=0:
#         new_nb+="-"
#
#     new_nb+=phone_nb[i]
#     i+=1
#
# print(new_nb)

#     #Zad3
# fav_dishes=input("Podaj swoje ulubione dania (oddziel je przecinkiem): ").split(",")
# i=0
# while i<len(fav_dishes):
#     print(f"Na {i+1} miejscu umieściłeś {fav_dishes[i]}")
#     i+=1

################################################
#FOR

    #Zad1
# warunek=''
# oceny=[]
# suma=0
# while warunek != 'X':
#     warunek=input("Podaj ocenę: \t Wpisz 'X' aby wyjść.")
#     if warunek != 'X':
#         oceny.append(warunek)
# print(oceny)
# for grade in oceny:
#     suma+=int(grade)
# print(f"Twoja średnia wynosi {suma/len(oceny)}.")

    #Zad2

# phone_nb=input("Podaj numer telefonu: ").replace("-","")
# new_nb=""
# print(len(phone_nb))
# for index, digit in enumerate(phone_nb):
#     if index %3 == 0 and index !=0:
#         new_nb+="-"
#     new_nb+=digit
# print(new_nb)

    #Zad3
# warunek=''
# suma=0
# wydatki={}
# while warunek !='N':
#     kat=input('Podaj kategorię wydatków: ')
#     kasa=input("Podaj ile na to wydałeś: ")
#     wydatki[kat]=int(kasa)
#     warunek=input("Czy wprowadzić kolejną kategorię? T/N ")
#
# print(wydatki)
# calkowite = sum([i for i in wydatki.values()])
# print(calkowite)
# for index, valu in wydatki.items():
#     print(f"{index} stanowi {valu/calkowite*100:.2f}% twoich wydatków.")
# print(f"Najwięcej wydajesz na {max(wydatki, key=wydatki.get)}")

##########################################################
#For in range

#     #Zad1
# phone_nb=input("Podaj swój numer telefonu: ").replace("-","")
# for digit in range(10):
#     print(f"W twoim numerze telefonu cyfra {digit} występuje {phone_nb.count(str(digit))}.")

    #Zad2
# print("Kalkulator kredytowy")
# loan=int(input("Podaj kwotę kredytu: "))
# rate=float(input("Podaj oprocentowanie: "))
# duration = int(input("Podaj czas trwania w latach: "))
# fees = int(input("Podaj koszty początkowe: "))
#
# monthly=loan/(duration*12)
# total=fees
# for month_nb in range(1,duration*12):
#     payment_left=loan-(month_nb-1)*monthly
#     monthly_fee=(payment_left*rate/100)/12+monthly
#     total+=monthly_fee
#     print(f"W {month_nb} miesiącu zapłacisz ratę w wysokości {monthly_fee:.2f}, pozostały do spłaty kapitał to {payment_left:.2f}.")
#     print(f"Zaciągając kredyt na {loan:.2f} w tych warunkach spłacisz razem {total:.2f} PLN.")

##############################################################
#Break Continue

    #Zad1
# grade_list=[]
# while True:
#     grade=input("Podaj ocenę lub wybierz X aby przerwać: ")
#     if grade == 'X':
#         break
#     grade_list+=grade
# print(grade_list)
# if grade_list.count('1')>0:
#     print("Niestety nie zdałeś.")
# else:
#     print("Brawo!")

#     #Zad2
# calkowite=0
# wydatki={}
# while True:
#     kat=input('Podaj kategorię wydatków lub wprowadź X aby przerwać: ')
#     if kat =="X":
#         break
#     wy]=[]
#     while True:
#         kasa=input("Podaj ile na to wydałeś lub wprowadź X aby przerwać: ")
#         if kasa == "X":
#             break
#         wydatki[kat].append(int(kasa))
#
# print(wydatki)
# for category in wydatki.values():
#     for wydatki_wart in category:
#         calkowite += wydatki[katdatki_wart
# print(calkowite)
#
# exp_perc={}
# total_cat_exp = 0
# for category, expend in wydatki.items():
#     for exp_val in expend:
#         total_cat_exp+=exp_val
#     exp_perc[category]=total_cat_exp*100/calkowite
#
# for index, valu in exp_perc.items():
#     print(f"{index} stanowi {valu/calkowite*100:.2f}% twoich wydatków.")
# print(f"Najwięcej wydajesz na {max(exp_perc, key=exp_perc.get)}")

    #Zad3
# num_list=[]
# while True:
#     grade=input("Podaj ocenę lub wybierz X aby przerwać: ")
#     if grade == 'X':
#         break
#     num_list+=grade
# print(num_list)
#
# for i in num_list:
#     if int(i) % 2 == 0:
#         continue
#     print(i)