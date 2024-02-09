#Int i float

# biedra = float(input("Podaj cenę jabłek w Biedronce:"))
# lidl = float(input("Podaj cenę jabłek w Lidlu:"))
# zabka = float(input("Podaj cenę jabłek w Żabce:"))
#
# cheapest = min(biedra,lidl,zabka)
#
# print("Najtańsze jabłka można kupić za",cheapest,"zł.")

#String

    #Zad1
# print("Obliczymy wartość Twojej lokaty!")
# start_val=int(input("Ile wpłaciłeś?"))
# percentage=int(input("Na jakie oprocentowanie?"))
# time=int(input("Na jak długo?"))
# final_val=start_val*(1+percentage/100)**time
# print(f"Twoja lokata będzie miała {final_val:.2f} zł.")

    #Zad2
# name = input("Jak masz na imię?")
# print(f"Twoje imię ma {len(name)} znaków.")

    #Zad3
# city_name=input("W jakim mieście mieszkasz?")
# print(f"Wow, super że mieszkasz w {city_name.title()}.")

    #Zad4

# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"
#
# print(f"Nr rejestracyjny\n Forda to {ford.upper()}, \n Audi to {audi.replace(' ','')},\n Citroena to {citroen.upper().replace("-","")}, \n Hondy to {honda}.")

#Listy

    #Zad1
# favourite_sports=['football','basketball','handball','tennis']
# print(f"Ulubiony sport to {favourite_sports[0]}, zas najmniej lubiany to {favourite_sports[-1]}.")
# favourite_sports[3] = "golf"
# print(favourite_sports)
#
#     #Zad2
# favourite_dish=[" "," "," "]
# dish=input("Podaj ulubioną potrawę:")
# favourite_dish[0]=dish
# dish=input("Podaj kolejną potrawę:")
# favourite_dish[1]=dish
# dish=input("Podaj kolejną potrawę:")
# favourite_dish[2]=dish
# print(f"Podałeś następujące potrawy: {favourite_dish}")

#     #Zad3
# phone_nb=input("Podaj swój numer telefonu:")
# print(phone_nb[:6]+"-"*3)

#Słowniki

#     #Zad1
# subjects={'matma':4.5,
#           'biola':3,
#           'polski':5,
#           'chemia':2}
# print(subjects)

#     #Zad2
# my_family={'name':"Szymon",
#            'surname':"B",
#            "birthday":"30-04",
#            "parents":[
#             {
#                 'name':"Ewa",
#                 'surname':"B",
#                 "birthday":"10-05",
#                 "parents":[]
#             },
#             {
#                 'name':"Janusz",
#                 'surname':"B",
#                 "birthday":"31-01",
#                 "parents":[]
#             }
#            ]
#            }
# print(my_family)

#     #Zad3
# wydatki={
#         "food":0.0,
#         "fun":0.0,
#         "bills":0.0,
#         "rest":0.0
#     }
#
# wydatki['food']=float(input("Ile wydajesz miesięcznie na jedzenie?"))
# wydatki['fun']=float(input("Ile wydajesz miesięcznie na imprezy?"))
# wydatki['bills']=float(input("Ile wydajesz miesięcznie na rachunki?"))
# wydatki['rest']=float(input("Ile wydajesz miesięcznie na inne?"))
#
# suma=wydatki['food']+wydatki['fun']+wydatki['bills']+wydatki['rest']
# kategoria=input(f"Podaj kategorię którą chcesz sprawdzić (list({wydatki.keys()})): ")
#
# perc_val=wydatki[kategoria]/suma*100
#
# print(f"Na {kategoria} wydajesz {perc_val}% swojego budżetu.")