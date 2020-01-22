import re

def halved(l):
    return [n / 2 for n in l]

print(halved([8, 4, 2]))

def only_positive(l):
    return [n for n in l if n > 0]

print(only_positive([9, -9, 7, -7, 4, -4]))

def total(l):
    return sum(l)

def stripped_strings(l):
    return [re.sub('\W', '', word) for word in l]

print(stripped_strings(['good', 'b!!!ad!!', 'Good_', 'B^$@AD']))

def find_special(l):
    for i in range(len(l)):
        if l[i] == 'special':
            return i
    return -1

def valid_contacts(l):
    return [contact for contact in l if len(contact['phone_number']) == 10]

contacts = [
  {"name": 'Reuben', "phone_number": '9196218777'},
  {"name": 'Laisha', "phone_number": '0123334766'},
  {"name": 'Cielo', "phone_number": '764'},
  {"name": 'Maya', "phone_number": '7653324599'}
]

print(valid_contacts(contacts))

def contact_names(l):
    return [contact['name'] for contact in l]

print(contact_names(contacts))