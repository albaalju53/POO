#Funcines como parametros
def inch2cm(x):
    return x*2.54

"""
def convert(x):
    y = inch2cm(x)
    print(x, '=>', y)

convert(3)
"""

def convert(f, x):
    y = f(x)
    print(x, '=>', y)

convert(inch2cm, 3)
