# lambda and higher order functions

addTwo = lambda num: num + num
print(addTwo(5))

sum_total = lambda a, b: a + b
print(sum_total(10, 8))

#################

def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addThirty = funcBuilder(30)

print(addTen(5))
print(addThirty(5))

#####################
# higher order functions - a function that takes one or more functions as arguments or returns a function as its result

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

##############



odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))


#########################

from functools import reduce


'''numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))'''

lambda acc, curr: acc + len(curr)

names = ["Perminus Karuri", "Benadatah Wanjiru Maina"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(f"\n{char_count}")