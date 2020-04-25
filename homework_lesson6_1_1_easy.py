#задача 1 easy

def avg(a,b):
    if a*b>=0:
        return(a*b)**0.5
    else:
        raise ValueError
try:
    a=float(input("a="))
    b=float(input("b="))
    c=avg(a,b)
    print("среднее геометрическое= {:.2f}".format(c))
except ValueError as error:
    print("ошибка",error)
except Exception as error:
    print("ошибка",error)
          
