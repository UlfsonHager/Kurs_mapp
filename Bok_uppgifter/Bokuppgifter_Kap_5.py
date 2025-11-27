<<<<<<< HEAD
# Bokuppgifter kap 5
# Nr 1 kodblock man kan anropa i programmet
# Nr 2 arguparametrarment defineras i funktionshuvudet, argument är det man skickar med när man anropar
# Nr 3
def upp_converter(instr):
    return(instr.upper())

retstr = upp_converter('hello')
print(retstr)                       

# Nr 4 
def add_subtract_funtion( a, b):
    return((a+b, a-b))

ret = add_subtract_funtion(5,2)
print(ret)
print(type(ret))


# Nr 5
def test_func(a, /,  b, *, c): # a är strikt position, b både och, c strikt keyword
    return(a + c)
retval= test_func(1, b=2, c=3)
print(retval)

#Nr 6 a tilldelas funtionen my_sum_.. och kan avnändas med samma argument

# Nr 7

def add_or_multiply(a, b, oper):
    if oper == '*':
        return a * b
    elif oper == '+':
        return a + b
    else :
        print('Wrong parameter use + or * ')
        return(-1)
    
print('Add 4 8, ', add_or_multiply(4,8,'+'))    
print('Multiply 4 8, ', add_or_multiply(4,8,'*'))    
print('Wrong call 4 8, ', add_or_multiply(4,8,'AAA'))    

# Nr 8
name = input('What is yor name ? ')
print('Your name is :', name)
=======
# Bokuppgifter kap 5
# Nr 1 kodblock man kan anropa i programmet
# Nr 2 arguparametrarment defineras i funktionshuvudet, argument är det man skickar med när man anropar
# Nr 3
def upp_converter(instr):
    return(instr.upper())

retstr = upp_converter('hello')
print(retstr)                       

# Nr 4 
def add_subtract_funtion( a, b):
    return((a+b, a-b))

ret = add_subtract_funtion(5,2)
print(ret)
print(type(ret))


# Nr 5
def test_func(a, /,  b, *, c): # a är strikt position, b både och, c strikt keyword
    return(a + c)
retval= test_func(1, b=2, c=3)
print(retval)

#Nr 6 a tilldelas funtionen my_sum_.. och kan avnändas med samma argument

# Nr 7

def add_or_multiply(a, b, oper):
    if oper == '*':
        return a * b
    elif oper == '+':
        return a + b
    else :
        print('Wrong parameter use + or * ')
        return(-1)
    
print('Add 4 8, ', add_or_multiply(4,8,'+'))    
print('Multiply 4 8, ', add_or_multiply(4,8,'*'))    
print('Wrong call 4 8, ', add_or_multiply(4,8,'AAA'))    

# Nr 8
name = input('What is yor name ? ')
print('Your name is :', name)
>>>>>>> 0e12af3e5bea5bb0d4423cd5a917b131e52781fd
