# using dictionaries to count letters in a word
def count_letters(word):
    counts = {}
    for letter in word:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    return counts

print(count_letters('Kajiado'))
print(count_letters('Nairobi'))

# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.

def email_list(domains):
    emails = []
    for domain,users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
        return (emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# updating contents of a dictionary using another dictionary
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

# another combining dictionary function
def combine_guests(guests1, guests2):
  new_dictionary = guests2
  new_dictionary.update(guests1)
  return new_dictionary

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
print(combine_guests(Rorys_guests, Taylors_guests))

# this function takes in a dictionary containing groups and their members
# and returns each member and the groups the are in
def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        # print(group,users)
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
            
    print(user_groups)
            
print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# Use a dictionary to count the frequency of letters in 
# the input string. Only letters should be counted, 
# not blank spaces, numbers, or punctuation. Upper 
# case should be considered the same as lower case. 
# For example, count_letters("This is a sentence.") 
# should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 
# 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
    result = {}
    for letter in text:
        if letter.isalpha() and letter != ' ':
            letter = letter.lower()
            if letter not in result:
                result[letter] = 0
            result[letter] += 1
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}