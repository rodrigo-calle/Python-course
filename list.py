#listas te permiten guarda un conjunto de elementos
#se usan square bracket []

bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)

#accesing elements
print(bicycle[-1])
print(bicycle[0])
#you can apply string methods
print(bicycle[1].title())
#using individual values from a list
message = f"My first message in {bicycle[1].title()}"
print(message)
#adding and removing elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
motorcycles.append('cross')
print(motorcycles)

car = []
car.append('toyota')
car.append('suzuki')
car.append('jeep')
print(car)
car.insert(0,'volvo')
print(car)

#removing an item using del statement
#funciona si conoces la posición
del car[0]
print(car)
#eliminar el último elemento
last_owned = car.pop()
print(last_owned)
#eliminar por nombre de elemento
people = ['rodrigo', 'cesar', 'valeria', 'gloria']
print(people)
people.remove('cesar')
print(people)
#sorting list
people.sort()
print(people)#esto hace que se ordene la lista alfabeticamente
people.sort(reverse=True)#inviente el orden
print(people)

people = ['rodrigo', 'cesar', 'valeria', 'gloria']
people.reverse()#invertir orden de lista
print(people)

#Tamaño de lista
print(len(people))