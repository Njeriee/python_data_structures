def get_word(sentence, n):
    if n > 0:
        sentence = sentence.split()
        n = n-1
        words = sentence[n]
        if n <= len(words):
            return words
        return "Nothing"

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1))


# list comprehensions
z = [x for x in range(0,101) if x%3==0]
print(z)

languages = ['python','c#','c++','javascript','php','ruby']
language_length = [len(language) for language in languages ]
print(language_length)

# enumerate
# returns a tuple of every element in the list containig 
# the index and the element
students = ['Ashley','Dylan','Kamau','Otieno']
for index, student in enumerate(students):
    print (student)
    # print ('{} - {}'.format(index +1 , student))

# Given a list of filenames, we want to rename all the files 
# with extension hpp to the extension h. To do this, we would 
# like to generate a new list called newfilenames, consisting 
# of the new filenames.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for name in filenames:
    if name.endswith('hpp'):
        name = name.split('.')
        name[1] = 'h'
        name = "{}.{}".format(name[0],name[1])
    newfilenames.append(name)
print(newfilenames)

# Let's create a function that turns text into pig latin: 
# a simple text transformation that modifies each 
# word moving the first character to the end and 
# appending "ay" to the end.For example, python 
# ends up as ythonpay.
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    pig_latin_word = word[1:] + word[0] + 'ay'
    say += pig_latin_word + ' '
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def group_list(group, users):
    members = group.split(",") 
    users = users
    # members = ''
    # for user in users:
    #     members += user + ',' + ' '
    # return "{}:{}".format(group,members)
    return type(members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


