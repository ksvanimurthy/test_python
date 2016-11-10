#   Print list items in gap of 2 and 3
list_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(list_string[1:8:2])
print(list_string[1:8:3])
print(type(list_string))    #    type() function to know which class a variable or a value belongs to


#   Write a program to print Fibonacci series: ******************This code is faster then using recursive function.**********
def fibonacci_series(num):
    fib_list = []
    for i in range(num):
        if i <= 1:
            fib_list.append(i)
        else:
            size = len(fib_list)
            fib_list.append((fib_list[size-1])+(fib_list[size-2]))
    return(fib_list)

#   Write a program to print Fibonacci series using recursive function:
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))

nterms = 20
if nterms<=0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))

print(fibonacci_series(10))


#   Write a program to print Factorial number:
def factorial_number(num):
    fact = 1
    if num ==0:
        return fact
    for n in range(1,num+1):
       fact = fact*n
    return fact
print(factorial_number(10))


#   Write a code to check given number is Prime or not.
def prime_number(num):
    if num<2:
        print("Given number is not a Prime number.")
    if num==2:
        print("Given number is a Prime number.")
    for i in range(2, int((num+1)/2)):
        if (num%i)==0:
            print(num+" is not a Prime number.")
            break
        else:
            print("Given number is a Prime number.")
        break

prime_number(5)

#   Create a new list of the town names using for loops... using list comprehensions... using the map() function.
towns = [{'name': 'Manchester', 'population': 58241},
         {'name': 'Coventry', 'population': 12435},
         {'name': 'South Windsor', 'population': 25709}]

#   Using for loop:
town_names = []
for town in towns:
    town_names.append(town.get('name'))
print(town_names)

#   Using list comprehensions:
town_names = [town.get('name') for town in towns]
print(town_names)

#   Using map() function
town_names = map(lambda town: town.get('name'), towns)
print(town_names)