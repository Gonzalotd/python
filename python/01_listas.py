squares = [1, 4, 9, 16, 25]
print(squares)

# Las listas se pueden indexar y segmentar
print( squares[0] ) # indexing returns the item
print( squares[-1] )
print( squares[-3: ]) # Slicing returns a new list

# Las listas también admiten operaciones como concatenación:
squares = squares + [36, 49, 64, 81, 100]
print( squares )

# Las listas son de tipo mutable, es decir, es posible cambiar su contenido:
cubes = [1, 8, 27, 65, 125]
number = 4 ** 3
print( number )
cubes[3] = number
print( cubes )

# Tu puedes agregar un nuevo items al final de la lista, usando el método list.append()
cubes.append(216)
cubes.append( 7 ** 3 )
print( cubes )

# La asignación simple en Python nunca copia datos, cualquier cambio que se realice en la lista 
# mediante una variable se reflejará en todas las demás variables que hacen referencia a ella.

rgb = ["Red", "Green", "Blue"]
rgba = rgb
print( id(rgb) == id(rgba) ) # True
rgba.append( "Alph" )
print( rgb )

# Es posible asignar a una rebanada
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print( letters )
# Replace some values
letters[2:5] = ['C', 'D', 'E']
print( letters )
# now remove them
letters[2:5] = []
print( letters )
# clear the list by replacing all the elements with an empty list
letters[:] = []
print( letters )

# Podemos conocer la longitud de las listas
letters = ['a', 'b', 'c', 'd']
print( len(letters) )

# Es Posible anidar lista
a = ['a', 'b', 'c', 'd']
n = [1, 2, 3]
x = [a, n]
print( x )
print( x[0] )
print( x[0][1] )