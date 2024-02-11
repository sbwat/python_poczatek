import random
def merger(*args):
    merged=''
    sep='-'
    for arg in args:
        merged += str(arg)+sep
    return merged[:-1]

def translate(**kwargs):
    print(kwargs)
    for name, value in kwargs.items():
        print(f"{name} = {value}")

def random_list():
    list=[]
    for _ in range(random.randint(0,10)):
        list.append(random.randint(0,10))
    return list

def unpacking():
    print(merger(1,5,8,"Marek",7,1))

    translate(imie="jacek", miasto="wawa", wiek=10)


    thd=[*random_list(),*random_list()]
    print(thd)

    first={"name":'Adam',
           "age":15,
           "city":'wwa'}
    second={"name2":'Ada',
           "age2":18,
           "city2":'lodz'}

    third= {**first,**second}
    print(translate(**third))





if __name__ == "__main__":
    unpacking()
