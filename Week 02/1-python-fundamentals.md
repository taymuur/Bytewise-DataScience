## Python Fundamentals

Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.

### Taking Input in Variable
```python
age = input('Enter your age: ')
```

### Type Casting
```python
birth_year = int(input('Enter your year of birth: '))
age = 2022 - birth_year
print('Age: ' + str(age))
```

### String Methods
* *upper*()
* *find*('substring')
* *replace*('substring', 'new-string')
* 'substring' *in* string

### Comparison & Logical Operators
* **Comaprison:** >, >=, ==, <, and <=
* **Logical:** *and*, and *or*

### Conditional Statements
```python
weight = int(input('Enter your weight: '))
unit = input("kg (K) or lbs (L): ")
if unit.upper() =='K':
  weight_conv = weight / 0.45
  print('Weight in Lbs:' + str(weight_conv))
elif unit.upper() == 'L':
  weight_conv = weight * 0.45
  print('Weight in kg:' + str(weight_conv))
else:
    print('Invalid unit is entered!')
```

### While Loop
```python
count = 1
while count <= 6:
  count += 2
  print(count)
```

### List Methods
* *append*(new-element)
* *insert*(new-element, index)
* *clear*()

### For Loop
```python
for i in range(start, end + 1):
  print(i)
```

### Tuples
* stores multiple items in a single variable
* items are ordered, unchangeable, and allow duplicate values
```python
my_tuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')

```
