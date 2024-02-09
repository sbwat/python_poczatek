#Instrukcje warunkowe i operatory logiczne

#BOOL

    #Zad1
# product1 = float(input("Podaj cenę pierwszego produktu:"))
# product2 = float(input("Podaj cenę drugiego produktu:"))
# product3 = float(input("Podaj cenę trzeciego produktu:"))
#
# print(f"Produkt pierwszy jest droższy od drugiego: \t\t {product1>product2}")
# print(f"Produkt pierwszy jest tańszy od drugiego: \t\t {product1<product2}")
# print(f"Produkt pierwszy jest droższy od trzeciego: \t\t {product1>product3}")
# print(f"Produkt pierwszy jest tańszy od trzeciego: \t\t {product1<product3}")

    #Zad2
# shopping_list=input("Wprowadź listę zakupów, produkty oddziel przecinkiem:")
# print(shopping_list)
#
# print(f"Twoja lista jest długa, ponieważ ma więcej niż 3 elementy \t\t {len(shopping_list.split(','))>3}")

    #Zad3

# print("Obliczymy wartość Twojej lokaty!")
# start_val=int(input("Ile wpłaciłeś?"))
# percentage=int(input("Na jakie oprocentowanie?"))
# time=int(input("Na jak długo?"))
# final_val=start_val*(1+percentage/100)**time
# print("Twoja lokata będzie miała",final_val)
# if final_val>start_val*1.1:
#     print(f"Gratuluję! Twoja lokata przyniesie więcej niż 10% zysku.")

###################################################################
#IF/ELSE

    #Zad1
# pc_price = float(input("Podaj cenę komputera:"))
# car_price = float(input("Podaj cenę samochodu:"))
# bike_price = float(input("Podaj cenę roweru:"))
#
# if pc_price>car_price:
#     print(f"Komputer jest droższy niż samochód")
# elif pc_price==car_price:
#     print("Komputer i samochód mają taką samą cenę.")
# else:
#     print("Komputer jest tańszy niż samochód")
#
# if bike_price>car_price:
#     print(f"Rower jest droższy niż samochód")
# elif bike_price==car_price:
#     print("Rower i samochód mają taką samą cenę.")
# else:
#     print("Rower jest tańszy niż samochód")
#
# if pc_price>bike_price:
#     print(f"Komputer jest droższy niż rower")
# elif pc_price==bike_price:
#     print("Komputer i rower mają taką samą cenę.")
# else:
#     print("Komputer jest tańszy niż rower")

    #Zad2
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
#
# if wydatki['food']>wydatki['fun']:
#     perc_val=wydatki['food']/suma*100
#     print(f"Najwięcej wydajesz na jedzenie. Wydajesz {perc_val:.2f}% swojego budżetu.")
# elif wydatki['fun']>wydatki['bills']:
#     perc_val=wydatki['fun']/suma*100
#     print(f"Najwięcej wydajesz na zabawę. Wydajesz {perc_val:.2f}% swojego budżetu.")
# elif wydatki['bills']>wydatki['rest']:
#     perc_val=wydatki['fun']/suma*100
#     print(f"Najwięcej wydajesz na rachunki. Wydajesz {perc_val:.2f}% swojego budżetu.")
# else:
#     perc_val=wydatki['rest']/suma*100
#     print(f"Najwięcej wydajesz na inne. Wydajesz {perc_val:.2f}% swojego budżetu.")

    #Zad3
# oceny = {}
# oceny['matematyka']=float(input("Podaj ocenę z matematyki:"))
# oceny['fizyka']=float(input("Podaj ocenę z fizyki:"))
# oceny['chemia']=float(input("Podaj ocenę z chemii:"))
# print(oceny)
# count_list=list(oceny.values())
# count = len([i for i in count_list if i < 2.0])
# if count >1 or (count ==1 and sum(count_list)/len(count_list)<3.5):
#     print("Przyko mi, nie zdałeś!")
# else:
#     print("Brawo, zdałeś!")
#
#     #Zad4
# name=input("Jak masz na imię?")
# if name[-1] =='a':
#     print("Jesteś kobietą.")
# else:
#     print("Jestes mężczyzną.")

##################################################################
#AND/OR/NOT

#     #Zad1
# kwota_kredytu=int(input("Podaj kwotę kredytu:"))
# oprocentowanie=float(input("Podaj oprocentowanie kredytu:"))
# wklad=int(input("Podaj wartość wkładu własnego:"))
# czas=int(input("Podaj czas kredytowania w latach:"))
# przychod=int(input("Podaj swój miesięczny przychód:"))
# wydatki=int(input("Podaj sumę swoich miesięcznych wydatków:"))
# rata=(kwota_kredytu*oprocentowanie/100)/12+kwota_kredytu/(czas*12)
# dostepne_srodki=przychod-wydatki
# nieruchomosc=wklad+kwota_kredytu
# wklad_perc=wklad*100/nieruchomosc
# if (wklad_perc>20 and dostepne_srodki-rata>1000) or (10<=wklad_perc<=20 and dostepne_srodki-rata>2000):
#     print(f'Możesz wziąć kredyt ponieważ twój wkład własny wynosi {wklad_perc:.1f}%, a miesięczne wolne środki wynoszą {dostepne_srodki - rata:.0f}zł.')
# else:
#     print("Nie stać Cię na kredyt")

####################################################################
#ELIF

    #Zad1
# mode=int(input("Wybierz funkcję: 1- lokata, 2 - kredyt "))
# if mode ==1:
#     print("Liczymy wartość lokaty. Podaj...")
# elif mode==2:
#     print("Liczymy wartość kredytu. Podaj....")
# else:
#     print("Wybrano nieobsługiwaną funkcję!")

    #Zad2
# print("Program zinterpretuje wyniki testu Coopera.")
# age=int(input("Podaj swój wiek: "))
# gender=int(input("Podaj swoją płeć (1-kobieta, 2-mężczyzna): "))
# score=int(input("Podaj swój wynik: "))
#
# if gender == 1:
#     if age==8:
#         if score>2190:
#             print("Bardzo dobrze!")
#         elif 1810<score<2180:
#             print("Dobrze")
#         elif 1800<score<1420:
#             print("Srednio")
#         elif 1050<score<1410:
#             print("Zle")
#         else:
#             print("Bardzo zle")

########################################################
#IN/IS

#     #Zad1
# shopping=input("Podaj listę zakupów, produkty rozdziel przecinkami").split(',')
# if 'chleb' in shopping or 'bułki' in shopping:
#     print("Lubisz chleb?")
# else:
#     print("Bez chelba i bułek?")

#     #Zad2
# phone_nb=input("Podaj swój numer telefonu:")
# if '0' in phone_nb:
#     print("Twoj nr tel zawiera 0")
# else:
#     print("Twoj numer nie zawiera 0")

#     #Zad3
# value=None
#
# if value is True:
#     print("Value jest True")
# elif value is False:
#     print("Value jest False")
# elif value is None:
#     print("Value jest None")
# else:
#     print("Value ma inną wartość")