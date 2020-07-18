#List Comprehensions

squares = []
for i in range(10):
  squares.append(i*i)

print(squares)

amounts = [32.45, 25.67, 4.56, 6.78]
TAX_RATE = .08

def get_final_price(amount):
  return amount * (1 + TAX_RATE)

final_prices = list(map 
(get_final_price, amounts))

#Using List Comprehensions
final_prices = [get_final_price(amount) for amount in amounts]

print(final_prices)

#List comprehensions are another way for us to make lists

squares = [i*i for i in range(10)]

print(squares)

#extending list comprehensions#by adding a conditional expression

#new_list = [expression for x in iterable (if conditional)]

sentence = 'the rocket came back from mars'
vowels = [letter for letter in sentence if letter in 'aeiou']

print (vowels)

numbers_list = [1.32, -9.32, 10.32, 11, -11.44]
numbers = [i if i > 0 else "negative" for i in numbers_list]
print(numbers)

#Set and Dictionary Comprehensions
dict1 = {"name": "cam"}
set1 = {"cam" , "cam", "camcam"}

list2 = ["cam", "camcam", "cam"]
tuple1 =("cam", "camcam", "cam")

quote = "don't worry about a thing!"
unique_vowels = {letter for letter in quote if letter in 'aeiou'}
print(unique_vowels)

#Dictionary Comprehension -

squares= {i: i*i for i in range (10)}
print(squares)
print(squares[0])
print(type(squares))


##Lambda Functions
#
#
#small anonymous functions stored as variables

#def pow_func(num, num2):
 # return num ** num2

pow_of = lambda num1, num2 : num1 ** num2

#print(pow_of(3,4))


pow_list={str(i): pow_of(i,i+2) for i in range(10)}
print(pow_list)






