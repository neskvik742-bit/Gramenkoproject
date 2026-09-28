# Перша програма
print("Hello World!")

# Створення змінних різних типів
name = "Nazar"          # str
age = 16                # int
height = 1.75           # float
is_student = True       # bool

# Інші типи
numbers = [1, 2, 3]     # list
coordinates = (10, 20)  # tuple
unique = {1, 2, 3}      # set
person = {"name": "Nazar", "age": 16}  # dict

# Виведення значень та їх типів
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(numbers, type(numbers))
print(coordinates, type(coordinates))
print(unique, type(unique))
print(person, type(person))

# Арифметичні оператори
a = 10
b = 3

print("Додавання:", a + b)
print("Віднімання:", a - b)
print("Множення:", a * b)
print("Ділення:", a / b)
print("Цілочисельне ділення:", a // b)
print("Остача:", a % b)
print("Степінь:", a ** b)

# Оператори порівняння
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Логічні оператори
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > b))

# Умовний оператор
if age >= 18:
    print("Повнолітній")
else:
    print("Неповнолітній")