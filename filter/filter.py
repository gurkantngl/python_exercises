from functools import reduce

numbers = [1,2,3,4,5]
numberSquare = list(map(lambda number: number**2, numbers))

numbersFilters = list(filter(lambda number: number>2, numbers))

print(numbers)
print(numbersFilters)

numbersFactorial = reduce(lambda x,y : x*y, numbers)

print(numbersFactorial)