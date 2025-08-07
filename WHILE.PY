def while1():
    x = 1 
    while x<=3:
        print(x)
        x=x+1
print ("-----------x---------")
#while1()

def while2():
    x = 1
    while x<=100:
        print(x)
        x=x+1
#while2()

def while3():
    x=50
    while x<=100:
        print(x)
        x=x+1
#while3()

def while4():
    x = 1
    while x <=10:
        print(x)
        x=x-1
    print ('fogo')
#while4()    
def numerospares():
    fim=int(input("Digite o último número a imprimir:"))               
    x = 0 
    while x <= fim:
        if x % 2 == 0: 
            print(x)
        x = x + 1
#numerospares()

def numerosimpares():
    fim=int(input("Digite o último número a imprimir:"))               
    x = 1
    while x <= fim:
        if x % 2 == 1: 
            print(x)
        x = x+1
numerosimpares()
