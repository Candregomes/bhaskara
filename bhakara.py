from math import sqrt
import math
a = float(input("Qual o valor de a?: "))
b = float(input("Qual o valor de b?: "))
c = float(input("Qual o valor de c?: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("esta equação não possui raízes reais")

if delta == 0:
    bhask1 = (-(b) + (math.sqrt(delta))) / (2*a)
    bhask2 = (-(b) - (math.sqrt(delta))) / (2*a)
    print("a raiz desta equação é",bhask1)

if delta > 0:
    bhask1 = (-(b) + (math.sqrt(delta))) / (2*a)
    bhask2 = (-(b) - (math.sqrt(delta))) / (2*a)
    if  bhask1 < bhask2:
        print("as raízes da equação são",bhask1,"e",bhask2)
    else:
        print("as raízes da equação são",bhask2,"e",bhask1)