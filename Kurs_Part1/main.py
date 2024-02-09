
time = 3
dinstance = 38
speed = dinstance / time
print("Srednia predkosc biegu to ", speed, "km/h.")

print("Moje ulubione dania to:","spaghetti","pizza", sep="\n")
#Zad1
age = input("Ile masz lat?")
print("To aż",int(age)*12,"miesięcy!")
#Zad2
dist = input("Ile kilometrów przeszedłeś w tym tygodniu?")
circ=40075/int(dist)
print("Obejscei ziemi zajmie Ci", circ, "tygodni!")
#Zad3
print("Obliczymy wartość Twojej lokaty!")
start_val=int(input("Ile wpłaciłeś?"))
percentage=int(input("Na jakie oprocentowanie?"))
time=int(input("Na jak długo?"))
final_val=start_val*(1+percentage/100)**time
print("Twoja lokata będzie miała",final_val)