# Python Modules and Packages

## Modules
* A moodule is a Python file containing Python statements and definitions.
* We put similar code in one module. This helps modularize our code and makes it much easier to deal with.
* A modules grants us *reusability*.
* A module’s contents are accessed with the `import` statement.

A file evenodd.py is a module, and we call it ‘evenodd’ module.
```python
def check():
         num = int(input('Enter a number: '))
         if num % 2 == 0: print("Even")
         else: print("Odd")
```

Some examples of modules are as follows:
```python
import math
from math import pi
math.pi
```

```python
import random
random.randint(1, 3)
```

## Pakages

* A Python package is nothing but a collection of modules along with a `__init__.py` file.
* The modules can also be arranged in hierarchy of folders inside a package.
* Just by adding an empty `__init__.py` file to the in the folder, Python knows it is a package.
* A Python package may contain several modules. To import one of these into your program, you must use the dot operator(.)

```python
import Game.Sound.load
```

```python
import Game.Level.start
```

```python
import random.randint(1, 3)
```


