import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

my_array = np.arange(15).reshape(3, 5)
print(my_array)

print(' 1 a)')
print(my_array.shape) # 3 rader och 5 kolumner

print(' 1 b')
print(my_array.size) # 15, storleken

print(' 1 c)')
print(my_array.mean()) # medelvärdet på hela

print(' 1 d)')
print(my_array.mean(axis=0)) # medelvärdet på alla kolumner

print(' 1 d)')
print(my_array.mean(axis=0)) # medelvärdet för resp kolumner

print(' 1 e)')
print(my_array.mean(axis=1)) # medelvärdet för resp rad

print(' 1 f)')
print(my_array.max()) # maxvärdet i arrayen

print(' 1 g)')
print(my_array.max(axis=0)) # maxvärdet i arrayen per kolumn

print(' 1 h)')
print(my_array.max(axis=1)) # maxvärdet i arrayen per rad


# Nr 2
data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name":["Alice", "Bob", "Charlie", "David", "Eve"],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [60000, 70000, 80000, 65000, 72000],
    "Hiredate": pd.to_datetime(["2023-01-10",
        "2018-02-20", "2021-03-15",
        "2001-04-25", "2016-05-30"]),
    "Fulltime": [True, True, False, True, False]
}

my_df = pd.DataFrame(data)
print(my_df)

# Nr 2
print()
print("2 a")
print(my_df.dtypes)# Skriver ut datatyper för respektive

print("2 b")
print(my_df.head(3))# Skriver ut de 3 första raderna

print("2 c")
print(my_df.loc[2:7, ['Name', 'Salary']])# 2 är offset och 7 är antal rader

print("2 d")
print(my_df.loc[:, ['Name']])# Skriver ut alla namn

print("2 e")
print(my_df["Salary"].mean()) # Skriver ut medel på lönen

print("2 f")
print(my_df["Salary"].min()) # Skriver ut minsta lönen

print("2 g")
print(my_df.describe()) # Skriver ut medel samt delen i % mellan min och max


# Nr 3 
""" Personligen tycker jag det explicita är mer läsbart, men jobbigare att skriva i
    och jag tror man föredra det implicita när man är produktiv i miljön"""
    
    
# Nr 4
print("Nr 4")

x = np.linspace(-4, 4, 10)
y = x**2
"""
fig, ax = plt.subplots()
ax.plot(x, y, '*-')
ax.set_title('y=x^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
visar grafen över en andragradsekvaktion där x har 10 punkter i intervallet -4 till 4"""


#Nr 5
print("Nr 5")

np.random.seed(15)
scatter_data_x = np.random.randn(1000)
scatter_data_y = np.random.randn(1000)
fruit_data = {'grapes': 22, 'apple': 8, 'orange': 15,
    'lemon': 20, 'lime': 25}
category = list(fruit_data.keys()) # Läser från dictonary namnen
values = list(fruit_data.values()) # Läser in värdena

# spridningsdigram
fig, axs = plt.subplots(1,2, figsize=(0,5)) # Storleken på fönstret
# plt.subplots returnerar 2 värden

axs[0].scatter(scatter_data_x, scatter_data_y)
axs[1].pie(x=values, labels=category) 
print(type(axs))
print(type(fig))
#plt.show()

