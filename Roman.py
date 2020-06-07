def romano(a):
    dicc = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X",9: "IX", 5: "V", 4: "IV", 1: "I"}
    palabra=''
    for x in dicc:
        while (a >= x) :
            a=a-x
            palabra=palabra+dicc[x]
    return  palabra

def Deromano(palabra):
    dicc = {"M":1000,"D":500, "C":100,  "L":50,  "X":10,  "V":5 , "I":1}
    numero=0
    for x in range(0,len(palabra)):
        if x < len(palabra)-1 :
            if dicc[palabra[x]] < dicc[palabra[x+1]]:
                numero=numero+dicc[palabra[x+1]]-dicc[palabra[x]]
                x=x+1
            else:
                numero = numero + dicc[palabra[x]]
        else:
            numero=numero+dicc[palabra[x]]
    return  numero




if __name__ == '__main__':
    print (Deromano(romano(2019)))
