# Chapter 3 from book

# Nr 1
age = 23
if age > 18:
    print('You can take driver license')
else: 
    print('You are too young')
    
# Detta är trivialt

# Nr 2
x = 33
if (x>10):
    print('större än 10')
elif (x<=10 and x>=5):
    print(' mellan 5-10')
elif (x<5):
    print('Mindre än 5')

# Nr 3 
# True är värdet 1, false värdet 0

# Nr 4
print(10 > 15) # printar ut false
# Nr 5
print(7 >= 7) # printar ut true
# Nr 6 
print(3 != 3) # printar ut false

# Nr 7
print(5 >=5 and 5 > 6)  # printar ut false

# Nr 8
print(5 >=5 or 5 > 6)  # printar ut true, ett villkor sant

# Nr 9
print((5 > 4 and 5 >= 5) or (10 >2 and 3 > 100)) # True första villkoret sant

# Nr 10, Frsta skriver ut både 10 och hundra, medan andra bara skriver ut 10 och sedan hoppar ut
number = 8
# Första
if number<5:
    print('Less than 5')
if number < 10:
    print('Less than 10')
if number < 100:
    print('Less than 100')
    
# Andra
if number<5:
    print('Less than 5')
elif number < 10:
    print('Less than 10')
elif number < 100:
    print('Less than 100')
