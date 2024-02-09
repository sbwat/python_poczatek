#FUNKCJE

    #Zad1
# def calculate_rectangle(a,b):
#     return float(a*b)
#
# a=float(input("Podaj długość pierwszego boku: "))
# b=float(input("Podaj długość drugiego boku: "))
#
# print(f"Pole powierzchni twojego prostokąta wynosi {calculate_rectangle(a,b)}")

    #Zad2
# def average(d,t):
#     return float(d/t)
#
# def user_input():
#     distance=float(input("Podaj pokonany dystans: "))
#     time=float(input("Podaj czas: "))
#     return(distance,time)
#
# print("Program wyznaczy średnią prędkość. Wybierz '1' dla biegu, '2' dla jazdy na rowerze, '3' dla jazdy samochodem.")
# mode=input("Wybierz tryb pracy: ")
# if mode =='1':
#     dist,time =user_input()
#     print(f"Średnia prędkość twojego biegu to {average(dist,time)} km/h.")
# elif mode == '2':
#     dist,time =user_input()
#     print(f"Średnia prędkość twojej jazdy na towerze to {average(dist,time)} km/h.")
# elif mode == '3':
#     dist, time = user_input()
#     print(f"Średnia prędkość twojej jazdy samochodem to {average(dist, time)} km/h.")
# else:
#     print("Wybrany tryb nie istnieje!")

    #Zad3
#
# def load_category():
#     wydatki={}
#     while True:
#         kat = input('Podaj kategorię wydatków lub wprowadź X aby przerwać: ')
#         if kat == "X":
#             return wydatki
#
#         wydatki[kat]=load_expend(kat)
#
# def load_expend(category):
#     wartosci=[]
#     while True:
#         kasa=input(f"Podaj ile wydałeś na {category} lub wprowadź X aby przerwać: ")
#         if kasa == "X":
#             return wartosci
#
#         wartosci.append(float(kasa))
#
# def total_expend(wydatki):
#     wynik=0
#     for category in wydatki.values():
#         wynik+=sum(category)
#     return wynik
#
# def expend_perc(wydatki,suma):
#     exp_perc={}
#     for category, expend in wydatki.items():
#         total_cat_exp = sum(expend)
#         exp_perc[category] = total_cat_exp * 100 / suma
#     return exp_perc
#
# def biggest_spend(perc_categories):
#     biggest=None
#     highest_perc=0
#     for category, percent in perc_categories.items():
#         if percent>highest_perc:
#             highest_perc=percent
#             biggest=category
#     return biggest, highest_perc
#
# def print_info(category, value):
#     print(f"Na {category} wydajesz {value:.1f}% swojego budżetu.")
#
# def print_highest(category, value):
#     print(f"Najwięcej wydajesz na {category}, jest to aż {value:.1f}% twojego miesięcznego budżetu!")
#
#
# wydatki=load_category()
# suma=total_expend(wydatki)
# procenty=expend_perc(wydatki,suma)
# mcat,mval = biggest_spend(procenty)
# if mcat is not None:
#     print_highest(mcat,mval)
# for category, perc in procenty.items():
#     print_info(category,perc)

#######################################################
#Argumenty pozycyjne i nazwane

#     #Zad1
# def average(d,t):
#     return float(d/t)
#
# def user_input():
#     distance=float(input("Podaj pokonany dystans: "))
#     time=float(input("Podaj czas: "))
#     return(distance,time)
#
# print("Program wyznaczy średnią prędkość. Wybierz '1' dla biegu, '2' dla jazdy na rowerze, '3' dla jazdy samochodem.")
# mode=input("Wybierz tryb pracy: ")
# if mode =='1':
#     dist,time =user_input()
#     print(f"Średnia prędkość twojego biegu to {average(d=dist,t=time)} km/h.")
# elif mode == '2':
#     dist,time =user_input()
#     print(f"Średnia prędkość twojej jazdy na towerze to {average(d=dist,t=time)} km/h.")
# elif mode == '3':
#     dist, time = user_input()
#     print(f"Średnia prędkość twojej jazdy samochodem to {average(d=dist, t=time)} km/h.")
# else:
#     print("Wybrany tryb nie istnieje!")

###############################################################
#Parametry domyślne

#     #Zad1
# def number_range(number,range=0.1):
#     minus_range=(1-range)*number
#     plus_range=(1+range)*number
#     print(f"Zakres dla {number} wynosi od {minus_range} do {plus_range}.")
#
# liczba=float(input("Podaj liczbę: "))
# number_range(liczba)

    #Zad2

# def class_list(name, myclass=None):
#     if myclass==None:
#         myclass=[]
#     names=name.spli(',')
#     for name in names:
#         myclass.append(name)
#     return myclass
#
# new_student=input("Podaj imiona uczniów, rozdziel je przecinkiem: ")
# dziennik=class_list(new_student)
# print(dziennik)