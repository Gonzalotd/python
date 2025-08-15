################
# sentencia if #
################

number = int(input("Ingrese un número entero: "))
if number < 0:
    print(f'El número {number} es menor a cero')
elif number == 0:
    print(f'El número ingresado es: {number}')
else:
    print(f'El número {number} es mayor a cero')

#################
# Sentencia for #
#################

words = ['cat', 'window', 'defenestrate']
for w in words:
    print( f'palabra: {w} -> longitu: {len(w)} ' )

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategía 1:  Iterar sobre una copia
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print( user ) # Se imprimer Éléonore

# Strategía 2: Creando una nueva colección
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print( active_users )

###################
# función range() #
###################

# Si se necesita iterar sobre una secuencia de números, es apropiado utilizar la función 
# integrada range(), la cual genera progresiones aritméticas:
for i in range(5):
    print(i)

lista1 = list(range(5,10))
print(lista1) # -> [5, 6, 7, 8, 9]

# va del 0 al 10 de 3 en 3
lista2 = list(range(0, 10, 3))
print(lista2) # -> [0, 3, 6, 9]

lista3 = list(range(-10, -100, -30))
print(lista3) # -> [-10, -40, -70]

# Para iterar sobre los índices de una secuencia, puedes combinar range() y len() así:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print( i, a[i])

# Decimos que tal objeto es iterable; esto es, que se puede usar en funciones y construcciones 
# que esperan algo de lo cual obtener ítems sucesivos hasta que se termine.

sumar = sum(range(4))
print(sumar) # -> 6

#########################
# else Clauses on Loops #
#########################
# En un bucle for, la cláusula else se ejecuta después de que el bucle termina su iteración final, 
# es decir, si no se produjo ninguna interrupción.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(f'{n} es un número primo')

######################
# La sentencia match #
######################
# Una sentencia match recibe una expresión y compara su valor con patrones sucesivos dados en uno o más bloques case.

def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case _: # '_' -> funciona como un comodin, si no encuentra la respuesta se ejecuta esta
            return 'Algo anda mal con Internet'
        
respuesta = http_error(409)
print( respuesta ) # Bad request

# Los cases se pueden combinar:
match status:
    case 401 | 403 | 404:
        print( 'Not allowed' )

# return -> solo se puede usar con una función

# point is an (x, y) tuple
"""
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")    
"""

# Con clases:
"""
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
"""

# También podemos usar con if
"""
match point:
    case Point(x, y) if x == y: # -> si es falso pasa al siguiente case
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
"""

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

#####################
# Definir funciones #
#####################
# La palabra reservada def es utilizada para definir las funciones en python, seguida del nombre de la función
# y si tiene parámetros deben de estar dentro del paréntesis.

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a + b
    print()

fib(100)

# num2 -> sería un valor opcional
def sumar(num1, num2=1):
    return num1 + num2

numero1 = 7
numero2 = 9

resultado = sumar(numero1, numero2)
print( f'La suma de {numero1} y {numero2} es {resultado}')

######################
# Expresiones lambda #
######################

# Las funciones Lambda pueden ser usadas en cualquier lugar donde sea requerido un objeto de tipo función. 
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)