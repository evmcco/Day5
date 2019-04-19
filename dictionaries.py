# Word Summary

#create a function that will take 2 indices, pull out the word between them and either add it to the dictionary or incremement it by one
def add_word_to_dict(i, letter_count):
    word = sentence[(i-letter_count):i]
    print(word)
    # letter_count = 0
    if word not in word_dict.keys():
        word_dict[word] = 1
    elif word in word_dict.keys():
        word_dict[word] += 1

sentence = input("Enter a sentence to parse: ")
word_dict = {}
#find each word using spaces
i = 0
letter_count = 0
print("length: %d" % len(sentence))
while i < len(sentence):
    if i == len(sentence) - 1:
        add_word_to_dict((i+1), (letter_count+1))
        # word = sentence[(i-letter_count):i]
        # print(word)
        letter_count = 0
    elif sentence[i] != " ":
        letter_count += 1
    elif (sentence[i] == " "):
        add_word_to_dict(i, letter_count)
        # word = sentence[(i-letter_count):i]
        # print(word)
        letter_count = 0
    print("i: %d l_c: %d" % (i, letter_count))
    i += 1
print(word_dict)


# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])


# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# phonebook_dict['Kareem'] = '938-489-1234'
# del phonebook_dict['Alice']
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

# digitalcrafts = {
#     'US': {
#         'Georgia': {
#             'Atlanta': '3423 Piedmonet Rd NE #415',
#         },
#         'Texas': {
#             'Houston': '3302 Canal St.'
#         }
#     }
# }

# print(digitalcrafts['US']['Georgia'])

# digitalcrafts['US']['Florida'] = {'Orlando': 'Communicore Epcot'}

# print(digitalcrafts['US']['Florida'])

# digitalcrafts['UK'] = {
#     'Surrey': {
#         'London': 'wherever'
#     }
# }

# countries = list(digitalcrafts.keys())
# cities = digitalcrafts['US'].keys()
# address = digitalcrafts.values()

# print(countries)
# print(cities)
# print(address)