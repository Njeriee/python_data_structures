# a function that returns string initials
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# formatting strings
name = 'Joy'
number = len(name) *5
# now formatting the strings into a sentence
print('Hello {}, your lucky number is {}'.format(name,number))

# you can use format in another way by placing variables at specfic place eg.
print('Your lucky number is {number}, {name}.'.format(name = name, number = number))
# using format within a function
def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name = name,grade = grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# format can also be used to define decimal digits to be displayed eg
price = 2.75
price_with_tax = price * 1.97
print(price, price_with_tax)
# to return a value upto to 2 decimal places one can use format
print("Base price: ${:.2f}\nTaxed_price: ${:.2f}".format(price,price_with_tax))

# formatting expressions can also be used to align text eg
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))

# now using a format expression to specify text alignment and decimal places
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
# the greater sign aligns text to the right at specified spaces i.e 3 and 6

# a palindrome function
def is_palindrome(input_string):
    new_str = ''
    rev_str = ''
    for i in input_string:
        if i != "":
            i = i.lower()
            new_str +=  i.strip()
            rev_str = i.strip() + rev_str
    if new_str == rev_str:return True
    return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def nametag(first_name, last_name):
	first_name = first_name
	last_name = last_name[0].upper()
	return("{first_name} {last_name}.".format(first_name = first_name,last_name= last_name))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

stra = "it's raining cats and cats"
str2 = stra.split()
print(str2[-1])
str2[-1] = 'dogs'
print(str2)
str3 = ' '.join(str2)
print(str3)

