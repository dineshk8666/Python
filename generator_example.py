"""
Generator:
    * No need to create a list variable
    * It dont store whole list in memory, instead it iterates one-by-one and fetch the value"
    * Reduce Usage of resources (system memory) as it just create a object, nothing get stored
    * Reduce the time of execution of the script/code
    * Can be also used with list comprehension
    * Make code easy readable
    ** Need to use inside the function


"""


def square_numbers(myNum):
    result =[]
    for num in myNum:
        result.append(num*num)
    return result

sq_numbers=square_numbers([1,2,3,4,5])
print sq_numbers

## Using Generator
def square_number_gen(myNum):
    for num in myNum:
        yield (num * num)
numbers = [1,2,3,4,5]
sq_numbers = square_number_gen(numbers)
print sq_numbers
print "First element of list:", next(sq_numbers)
print "\n"
print "Iterates Remaining Element of list:" 
for num in sq_numbers:
    print num

print "\n"
## List comprehension
print "List Comprehension way:"
numbers = [1,2,3,4,5]
square_numbers = [ x * x for x in numbers]
print square_numbers

print "\n"
## Using  Generator with list comprehension
print "Creating Generator with List Comprehension way:"
numbers = [1,2,3,4,5]
## To use generator replace list parenthesis ([]) with square_parenthesis (())
square_numbers = ( x * x for x in numbers)
print square_numbers

## Print generator as whole list , but this loose the benefits of using generator in terms of performance as it consume large memory to store full list of elements specially when it is a large size list 
print list(square_numbers)

## print list element with iteration
for num in square_numbers:
    print num
