num_1 = 5
num_2 =3
my_result =num_1+num_2
print("Add ", my_result)

number_1 = 10
number_2 = 7
my_mult_result=number_1*number_2
print("Mult ", my_mult_result)

# Modulus, returnerar rest vid division
print("Modulus 10 % 3 = ", 10 % 3)

# heltals division tar bara heltalet , icke avrundat
print("27 // 6 heltal= ",27 // 6)

print('it\'s fun to learn!')

# Detta HAHAHA
print("HA"*3)

full_name = "Anna Andersson"
# Skriver ut Anna
print(full_name[0:5])

# Skriver ut längden på strängen
print("Längd =", len(full_name))
      

founder = "Guido van Rossum"
language = "Python"
print(f"Hello {founder}, {language} is fun to learn")

first_tuple = (10,5,'hi',3)
# first_tuple[1] = 10 går ej immutable

my_tuple = ('languages', ['Python', 'Java', 'C', 'R'],
        'apples')
print(my_tuple[0]) # Första
print(my_tuple[-1]) # sista
print(my_tuple[1][2]) # C


print(type(my_tuple)) # Type

my_first_list = [10, 5, 'hi', 3]
my_first_list[1] = 10
print(type(my_first_list)) # Type of my_first_list

shopping_list = ['apple', 'banana', 'grapes', 'eggs', 
                 'milk'] 
print("Längd ", len(shopping_list))
shopping_list.append('bread')
print(shopping_list)

my_numbers = [1, 7, 2, 7, 10, 7]
print("Antal i lista",  my_numbers.count(7)) # Antal 7 

one_tuple = (10, 5, 3)
one_list = list(one_tuple)

my_first_dict = {'Anna':38, 'Goran':19, 'Lennart':
                 59, 'Hali':28}
my_first_dict['Goran']
print(' Type dict ',type(my_first_dict)) # Type of my_first_dict
print(my_first_dict['Goran'])

my_set = {10, 5, 2, 5, 5}
print(my_set) # Endast unika element i set

A = {1, 2, 3, 4, 5}
B = {3, 10, 5, 7}

print("Intersection A on B",A.intersection(B))
print("Union A on B",A.union(B))
print("Difference A on B",A.difference(B))

list_a = [1, 2, 3, 4, 5] 
list_b = [5, 6, 10, 1]
list_c = list_a + list_b # Detta fungerade
print("Båda listorna ", list_c)
#Städa bort dubletter
set_a = set(list_c)
print("Utan dubletter ", set_a)

duplicate_values = (10, 2, 2, 10, 1)
set_b = set(duplicate_values)
print("set_b Utan dubletter ", set_b)