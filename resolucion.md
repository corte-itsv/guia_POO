# Soluciones Ejercicios de Programación Orientada a Objetos (OOP) en Python

## Ejercicio 1: Definir una clase Vehicle vacía

```python
class Vehicle:
    pass


print(Vehicle)
```

- **`class Vehicle:`**: Declara una nueva clase llamada `Vehicle`. Los dos puntos marcan el inicio del cuerpo de la clase.
- **`pass`**: Un marcador de posición que no hace nada, pero satisface el requisito de Python de que el cuerpo de una clase no esté vacío. No hace nada en tiempo de ejecución, pero evita un `SyntaxError`.
- **`print(Vehicle)`**: Imprime el objeto clase en sí, confirmando que fue creado correctamente. La salida muestra el nombre de la clase y el módulo al que pertenece (`__main__` cuando se ejecuta como script).

---

## Ejercicio 2: Clase Vehicle con atributos de instancia

```python
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")
```

- **`def __init__(self, name, max_speed, mileage)`**: El método constructor, llamado automáticamente cuando se crea un nuevo objeto. `self` hace referencia a la instancia específica que se está inicializando.
- **`self.name = name`**: Vincula el argumento pasado durante la creación del objeto a la instancia, haciéndolo accesible como atributo en ese objeto.
- **`vehicle1 = Vehicle("Tesla Model S", 250, 18)`**: Crea una nueva instancia de `Vehicle`. Python pasa los argumentos a `__init__` automáticamente.
- **`vehicle1.max_speed`**: Se usa notación de punto para acceder a los atributos de instancia. Cada objeto mantiene su propia copia de estos valores.

---

## Ejercicio 3: Clase Rectangle con área y perímetro

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 4)
print("Area =", rect.area())
print("Perimeter =", rect.perimeter())
```

- **`def area(self)`**: Un método de instancia que usa `self.length` y `self.width` para calcular y retornar el área. El parámetro `self` le da al método acceso a los atributos propios del objeto.
- **`def perimeter(self)`**: Aplica la fórmula estándar del perímetro de un rectángulo: `2 * (length + width)`. Al igual que `area()`, lee directamente de los atributos de la instancia.
- **`rect.area()`**: Al llamar a un método sobre una instancia, esa instancia se pasa automáticamente como `self`. No es necesario pasar `self` explícitamente al llamar al método.

---

## Ejercicio 4: Clase Student con promedio de notas

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum(self.marks) / len(self.marks)


s1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"{s1.name}'s Average Grade: {s1.average()}")
```

- **`self.marks = marks`**: Almacena la lista completa como atributo de instancia. Cada objeto `Student` mantiene su propia lista independiente de notas.
- **`sum(self.marks)`**: Usa la función incorporada `sum()` de Python para sumar todos los elementos de la lista de notas sin necesidad de un bucle explícito.
- **`len(self.marks)`**: Retorna la cantidad de elementos de la lista, usada como divisor para calcular la media. Esto funciona correctamente sin importar cuántas notas se almacenen.
- **`s1.average()`**: Llama al método sobre la instancia. El resultado es un flotante, porque el operador `/` de Python 3 siempre retorna un flotante.

---

## Ejercicio 5: Clase Product con calculadora de valor de stock

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


p1 = Product("Laptop", 899.99, 5)
print(f"Total stock value of {p1.name}: ${p1.total_value():.2f}")
```

- **`self.price` y `self.quantity`**: Se almacenan como atributos de instancia, de modo que cada objeto `Product` lleva el control de su propio precio y nivel de stock de forma independiente.
- **`def total_value(self)`**: Un método calculado que multiplica `self.price` por `self.quantity` para obtener el valor total del stock. No se necesitan datos externos porque todos los valores ya están en la instancia.
- **`:.2f`**: Un especificador de formato dentro de un f-string que redondea el flotante a exactamente dos decimales, que es el formato estándar para mostrar valores monetarios.

---

## Ejercicio 6: BankAccount con depósito y protección contra sobregiro

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")


account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
```

- **`self.balance += amount`**: El método `deposit()` modifica directamente el `balance` de la instancia. Como el atributo se almacena en `self`, el cambio persiste en todas las llamadas futuras a métodos sobre ese objeto.
- **`if amount <= self.balance`**: Protege el retiro verificando que existan fondos suficientes antes de modificar el saldo. Esto impone la regla de negocio de que el saldo no puede volverse negativo.
- **`else: print(...)`**: Da retroalimentación cuando un retiro es rechazado. En una aplicación real esto podría lanzar una excepción personalizada, pero un mensaje impreso es apropiado para un ejercicio introductorio.

---

## Ejercicio 7: Clase Light con alternancia de estado encendido/apagado

```python
class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        self.is_on = False
        print("Light is OFF")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current status: {state}")


light = Light()
light.turn_on()
light.status()
light.turn_off()
light.status()
```

- **`self.is_on = False`**: Establece el estado inicial de la luz como apagada cuando el objeto se crea por primera vez. Usar un booleano es la forma más directa de representar una condición de dos estados como encendido/apagado.
- **`turn_on()` y `turn_off()`**: Cada método simplemente cambia `self.is_on` al valor booleano apropiado e imprime un mensaje. Como el valor se almacena en `self`, el cambio se conserva en todas las llamadas subsecuentes a los métodos.
- **`"ON" if self.is_on else "OFF"`**: Una expresión ternaria de Python que convierte el estado booleano en una cadena legible. Es más conciso que escribir un bloque `if/else` completo para una salida simple de dos ramas.

---

## Ejercicio 8: Clase User con validación de contraseña

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password


u1 = User("alice", "secure123")
print(u1.check_password("secure123"))
print(u1.check_password("wrongpass"))
```

- **`self.password = password`**: Almacena la contraseña como atributo de instancia. En aplicaciones reales nunca se almacenaría una contraseña en texto plano; en su lugar se hashearía usando una librería como `bcrypt`. Aquí se usa texto plano para mantener el foco en los fundamentos de OOP.
- **`def check_password(self, input_password)`**: Acepta una contraseña candidata y la compara con la almacenada. Exponer un método en lugar del atributo directamente significa que el código externo nunca necesita tocar `self.password` directamente.
- **`return self.password == input_password`**: La comparación `==` evalúa a un booleano, por lo que el resultado puede retornarse directamente sin envolverlo en un `if/else` explícito.

---

## Ejercicio 9: Clase Temperature con conversores de unidades

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

t = Temperature(100)
print("Celsius:", t.celsius)
print("Fahrenheit:", t.to_fahrenheit())
print("Kelvin:", t.to_kelvin())
```

- **`self.celsius = celsius`**: La única fuente de verdad para este objeto. Ambos métodos de conversión derivan sus resultados de este único atributo, por lo que actualizarlo afectaría automáticamente todas las conversiones.
- **`(self.celsius * 9 / 5) + 32`**: La fórmula estándar de Celsius a Fahrenheit. En Python 3, `9 / 5` evalúa a `1.8` como flotante, por lo que el resultado siempre es un número decimal.
- **`self.celsius + 273.15`**: La conversión de Celsius a Kelvin suma el desplazamiento del cero absoluto. Sumar un literal flotante garantiza que el valor retornado siempre sea un flotante, en consonancia con la notación científica.

---

## Ejercicio 10: Clase Notebook con agregado y visualización de notas

```python
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")


nb = Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_notes()
```

- **`self.notes = []`**: Inicializar la lista dentro de `__init__` es fundamental. Si se definiera a nivel de clase en su lugar, todas las instancias compartirían la misma lista, causando que las notas de un cuaderno aparecieran en otro.
- **`self.notes.append(note)`**: Modifica en el lugar la propia lista de la instancia. Cada llamada a `add_note()` hace crecer la lista en una entrada, y el cambio persiste en el objeto hasta que se destruye.
- **`enumerate(self.notes, start=1)`**: Produce pares de `(índice, valor)` comenzando desde 1, permitiendo que el bucle imprima una lista numerada sin llevar manualmente el conteo con una variable.

---

## Ejercicio 11: CoffeeMachine con seguimiento de múltiples recursos

```python
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def make_latte(self):
        water_needed = 200
        coffee_needed = 20
        milk_needed = 150

        if self.water >= water_needed and self.coffee >= coffee_needed and self.milk >= milk_needed:
            self.water -= water_needed
            self.coffee -= coffee_needed
            self.milk -= milk_needed
            print(f"Latte made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml")
        else:
            print("Not enough resources to make a latte.")


machine = CoffeeMachine(water=300, coffee=100, milk=200)
machine.make_latte()
machine.make_latte()
```

- **`water_needed`, `coffee_needed`, `milk_needed`**: Definidas como variables locales dentro del método para representar la receta. Mantenerlas locales (en lugar de escribirlas fijas dentro de la condición) hace que el método sea más fácil de leer y los valores fáciles de cambiar en un solo lugar.
- **`if self.water >= water_needed and ...`**: Las tres verificaciones de recursos se combinan en una sola condición usando `and`. El descuento solo ocurre cuando se cumplen todas las condiciones, lo que evita un consumo parcial de recursos ante un intento fallido.
- **`self.water -= water_needed`**: Modifica el atributo de instancia en el lugar. Después de un latte exitoso, el estado de la máquina se actualiza permanentemente, por lo que una segunda llamada a `make_latte()` refleja los niveles reducidos.
- **Segunda llamada a `make_latte()`**: Con solo `100ml` de agua restante (menos que los `200ml` requeridos), la condición falla y se imprime el mensaje de recursos insuficientes, demostrando la persistencia del estado entre llamadas.

---

## Ejercicio 12: Atributo de clase compartido entre instancias

**Solución y explicación:**

```python
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)

print(f"{v1.name} - Color: {v1.color}, Speed: {v1.max_speed}")
print(f"{v2.name} - Color: {v2.color}, Speed: {v2.max_speed}")

Vehicle.color = "Red"

print(f"{v1.name} - Color: {v1.color}, Speed: {v1.max_speed}")
print(f"{v2.name} - Color: {v2.color}, Speed: {v2.max_speed}")
```

- **`color = "White"`**: Declarado a nivel de clase, fuera de `__init__`. Esto significa que pertenece a la clase misma, no a ninguna instancia individual. Todos los objetos comparten el mismo valor a menos que lo sobrescriban individualmente.
- **`v1.color`**: Cuando Python busca `color` en una instancia y no lo encuentra como atributo de instancia, sube hasta la clase y lo encuentra ahí como atributo de clase. Esta cadena de búsqueda forma parte del orden de resolución de atributos de Python.
- **`Vehicle.color = "Red"`**: Reasignar mediante el nombre de la clase actualiza el atributo a nivel de clase, por lo que todas las instancias que aún dependan del atributo de clase reflejan inmediatamente el nuevo valor. En cambio, hacer `v1.color = "Red"` solo crearía un nuevo atributo de instancia en `v1`, sin afectar a `v2`.

---

## Ejercicio 13: Subclase Bus que hereda de Vehicle

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

class Bus(Vehicle):
    pass

bus1 = Bus("School Bus", 120)
bus1.display()
```

- **`class Bus(Vehicle):`**: Los paréntesis indican que `Bus` hereda de `Vehicle`. Python configura la cadena de herencia automáticamente, lo que significa que `Bus` obtiene todos los atributos y métodos de `Vehicle` de forma gratuita.
- **`pass`**: Como `Bus` no agrega ningún comportamiento nuevo en esta etapa, se usa `pass` como marcador de posición. La clase sigue siendo completamente funcional porque todo lo que necesita viene de `Vehicle`.
- **`bus1.display()`**: Python primero busca `display` en la instancia de `Bus`, luego en la clase `Bus`, y finalmente en `Vehicle`, donde encuentra y ejecuta el método. Este proceso de búsqueda se conoce como Orden de Resolución de Métodos (MRO).

---

## Ejercicio 14: Sobrescribir un método del padre usando super()

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        print(f"{self.name} seating capacity is: {capacity}")

class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)

bus = Bus("School Bus", 120)
bus.seating_capacity()
```

- **`def seating_capacity(self, capacity)` en `Vehicle`**: El padre define el método para aceptar un valor de capacidad flexible, manteniéndolo lo suficientemente general para funcionar con cualquier tipo de vehículo.
- **`def seating_capacity(self)` en `Bus`**: El hijo sobrescribe el método con una versión que no recibe argumento de capacidad. Esta es la sobrescritura: cuando se llama a `seating_capacity()` sobre una instancia de `Bus`, Python ejecuta esta versión en lugar de la del padre.
- **`super().seating_capacity(50)`**: `super()` retorna un proxy hacia la clase padre, permitiendo que el hijo llame directamente al método del padre. El `50` fijo es el valor por defecto específico del bus, pasado hacia arriba a la implementación del padre para que la lógica de impresión permanezca en un solo lugar.
- **`bus.seating_capacity()`**: Se llama sin argumentos sobre la instancia de `Bus`. La sobrescritura intercepta la llamada, provee el valor por defecto de `50`, y delega la salida real al padre, combinando el comportamiento de ambas clases de forma limpia.

---

## Ejercicio 15: Agregar tarifa de mantenimiento en clase hija vía super()

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee = base_fare * 0.10

    def total_fare(self):
        return self.base_fare + self.maintenance_fee

taxi = Taxi(500)
print("Total fare with maintenance fee:", taxi.total_fare())
```

- **`class Vehicle`**: Define la clase padre que acepta y almacena `base_fare` en su constructor.
- **`super().__init__(base_fare)`**: Llama al constructor del padre desde dentro de la clase hija, asegurando que `self.base_fare` quede correctamente establecido antes de que el hijo agregue su propia lógica.
- **`self.maintenance_fee = base_fare * 0.10`**: Calcula la tarifa de mantenimiento del 10% y la almacena como un atributo exclusivo del hijo.
- **`total_fare()`**: Retorna la suma de la tarifa base y la tarifa de mantenimiento, demostrando cómo las clases hijas pueden extender el comportamiento del padre sin modificarlo.

---
## Ejercicio 16: Polimorfismo con speak() en Dog y Cat

**Solución y explicación:**

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())
```

- **`class Animal`**: Actúa como clase base con un método `speak()` por defecto, estableciendo una interfaz común para todas las subclases.
- **`class Dog(Animal)`**: Hereda de `Animal` y sobrescribe `speak()` para retornar `"Woof!"`, reemplazando la implementación genérica del padre.
- **`class Cat(Animal)`**: De forma similar, sobrescribe `speak()` para retornar `"Meow!"`.
- **Sobrescritura de métodos**: Cuando se llama a `speak()` sobre un objeto `Dog` o `Cat`, Python usa la versión de la subclase, no la del padre. Este es el fundamento del polimorfismo.

---

## Ejercicio 17: Lógica de pago para empleados de tiempo completo vs medio tiempo

**Solución y explicación:**

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_pay(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 12

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked


ft = FullTimeEmployee("Alice", 60000)
pt = PartTimeEmployee("Bob", 500, 20)

print(f"{ft.name}'s monthly pay: {ft.calculate_pay()}")
print(f"{pt.name}'s monthly pay: {pt.calculate_pay()}")
```

- **`class Employee`**: Sirve como clase base que contiene el atributo compartido `name` y un `calculate_pay()` por defecto que retorna `0`.
- **`FullTimeEmployee.calculate_pay()`**: Divide el salario anual entre 12 para obtener el pago mensual, usando el operador `/` de Python 3, que retorna un flotante.
- **`PartTimeEmployee.calculate_pay()`**: Multiplica `hourly_rate` por `hours_worked`, modelando un contrato de pago por hora.
- **`super().__init__(name)`**: Usado en ambas subclases para delegar la asignación de `name` al padre, evitando la duplicación de código.

---

## Ejercicio 18: Subclases Shape con métodos area() personalizados

**Solución y explicación:**

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(7), Square(4), Triangle(6, 8)]
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area()}")
```

- **`class Shape`**: Proporciona una interfaz común con un `area()` por defecto que retorna `0`. Se espera que todas las subclases sobrescriban este método.
- **`Circle.area()`**: Aplica la fórmula `pi * r^2`. El resultado se redondea a 2 decimales usando `round()` para una salida limpia.
- **`Square.area()`**: Retorna `side ** 2`, la fórmula de área más simple.
- **`type(shape).__name__`**: Obtiene dinámicamente el nombre de la clase de cada objeto en tiempo de ejecución, haciendo reutilizable el bucle de impresión sin necesidad de escribir los nombres a mano.

---

## Ejercicio 19: Subclases Media con atributos específicos por tipo

**Solución y explicación:**

```python
class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def describe(self):
        return f"{self.title} - Rs.{self.price}"

class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author

    def describe(self):
        return f"Book: {self.title} by {self.author} - Rs.{self.price}"

class Magazine(Media):
    def __init__(self, title, price, frequency):
        super().__init__(title, price)
        self.frequency = frequency

    def describe(self):
        return f"Magazine: {self.title} ({self.frequency}) - Rs.{self.price}"

class DVD(Media):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self.duration = duration

    def describe(self):
        return f"DVD: {self.title}, {self.duration} mins - Rs.{self.price}"


items = [
    Book("Clean Code", 499, "Robert C. Martin"),
    Magazine("Wired", 150, "Monthly"),
    DVD("Inception", 299, 148)
]

for item in items:
    print(item.describe())
```

- **`class Media`**: Almacena los atributos compartidos `title` y `price`, comunes a todos los tipos de medios, y proporciona un `describe()` genérico como respaldo.
- **`super().__init__(title, price)`**: Usado en cada subclase para evitar repetir la asignación de los atributos compartidos, manteniendo el código DRY (No te Repitas).
- **Atributos únicos**: `author`, `frequency` y `duration` son específicos de cada subclase y no pertenecerían a la clase base, ya que no todos los tipos de medios los comparten.
- **Iterar con `describe()`**: Llamar al mismo método en distintos objetos y obtener distintas salidas es polimorfismo en la práctica.

---

## Ejercicio 20: Subclase DiscountedOrder con 10% de descuento

**Solución y explicación:**

```python
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

    def get_total(self):
        return self.total

class DiscountedOrder(Order):
    def __init__(self, order_id, total):
        super().__init__(order_id, total)

    def get_total(self):
        return self.total * 0.90


order = DiscountedOrder("ORD001", 1200)
print("Order ID:", order.order_id)
print("Original Total:", order.total)
print("Discounted Total:", order.get_total())
```

- **`class Order`**: La clase padre almacena `order_id` y `total`, y `get_total()` simplemente retorna el monto completo sin ninguna modificación.
- **`DiscountedOrder.get_total()`**: Sobrescribe el método del padre para aplicar una reducción del 10% multiplicando `self.total` por `0.90`. La clase padre nunca se modifica.
- **`order.total` vs `order.get_total()`**: Acceder directamente a `self.total` sigue retornando el valor original, mientras que `get_total()` retorna el valor con descuento. Esta distinción es importante para mantener intactos los datos originales.
- **Principio de abierto/cerrado**: La clase `Order` está cerrada a la modificación pero abierta a la extensión. `DiscountedOrder` la extiende sin tocar el código original.

---

## Ejercicio 21: Jerarquía de clases Vehicle con Bike, Truck y Bus

**Solución y explicación:**

```python
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def describe(self):
        print(f"{type(self).__name__} max speed: {self.max_speed} km/h")

class Bike(Vehicle):
    def __init__(self):
        super().__init__(120)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(90)

class Bus(Vehicle):
    def __init__(self):
        super().__init__(100)


vehicles = [Bike(), Truck(), Bus()]
for v in vehicles:
    v.describe()
```

- **`class Vehicle`**: Acepta `max_speed` como parámetro y proporciona un método `describe()` compartido usado por todas las subclases.
- **Constructores de las subclases**: Cada subclase fija su propio valor de `max_speed` y lo pasa hacia el padre mediante `super().__init__()`. No se necesitan atributos adicionales en las subclases.
- **`type(self).__name__`**: Dentro del `describe()` de la clase base, esto obtiene el nombre real de la clase en tiempo de ejecución (`Bike`, `Truck` o `Bus`), haciendo el método reutilizable sin necesidad de sobrescribirlo en cada subclase.
- **Recorrer una lista mixta**: Los tres objetos se almacenan en una sola lista y se recorren de manera uniforme, un ejemplo directo de comportamiento polimórfico.

---

## Ejercicio 22: Identificar la clase de un objeto usando type()

**Solución y explicación:**

```python
class Dog:
    pass

class Cat:
    pass

class Vehicle:
    pass


d = Dog()
c = Cat()
v = Vehicle()

objects = {"d": d, "c": c, "v": v}

for name, obj in objects.items():
    print(f"{name} is of type: {type(obj).__name__}")
```

- **`class Dog: pass`**: La palabra clave `pass` crea un cuerpo de clase válido pero vacío. Esto es útil cuando la estructura de la clase no es relevante para el objetivo del ejercicio.
- **`type(obj)`**: Retorna la clase (objeto de tipo) a partir de la cual se creó `obj`. Por ejemplo, `type(d)` retorna `<class '__main__.Dog'>`.
- **`type(obj).__name__`**: El atributo `.__name__` sobre el objeto de tipo retornado da solo el nombre simple de la clase como cadena, como `"Dog"`, sin el prefijo del módulo.
- **Alternativa – `isinstance()`**: Mientras que `type()` verifica la clase exacta, `isinstance(d, Dog)` también retorna `True` para subclases. Usa `type()` cuando necesites una coincidencia exacta, e `isinstance()` cuando la herencia deba tenerse en cuenta.

---

## Ejercicio 23: Verificación de tipos con isinstance() e issubclass()

**Solución y explicación:**

```python
class Animal:
    pass

class Dog(Animal):
    pass


d = Dog()

print("Is d an instance of Dog?", isinstance(d, Dog))
print("Is d an instance of Animal?", isinstance(d, Animal))
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
print("Is Animal a subclass of Dog?", issubclass(Animal, Dog))
```

- **`isinstance(d, Dog)`**: Retorna `True` porque `d` fue creado directamente a partir de la clase `Dog`.
- **`isinstance(d, Animal)`**: También retorna `True` porque `Dog` hereda de `Animal`. Esta conciencia de la herencia es lo que hace que `isinstance()` sea más útil que una comparación directa con `type()` en la mayoría de los escenarios reales.
- **`issubclass(Dog, Animal)`**: Retorna `True` porque `Dog` está definida con `Animal` como su padre. Esto funciona sobre las clases mismas, no sobre las instancias.
- **`issubclass(Animal, Dog)`**: Retorna `False` porque la relación es unidireccional. El padre no hereda del hijo.

---

## Ejercicio 24: Suma de vectores usando sobrecarga de __add__

**Solución y explicación:**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 1)

result = v1 + v2
print(result)
```

- **`__add__(self, other)`**: Python llama a este método automáticamente cuando se usa el operador `+` entre dos objetos `Vector`. `self` es el operando izquierdo y `other` el derecho.
- **Retorna un nuevo `Vector`**: En lugar de modificar `self` en el lugar, el método crea y retorna un objeto `Vector` nuevo. Esto mantiene los objetos inmutables bajo la suma, que es el comportamiento esperado para tipos matemáticos.
- **`__repr__`**: Define la representación en cadena del objeto usada por `print()` y por la consola interactiva. Sin él, `print(result)` mostraría algo como `<__main__.Vector object at 0x...>`.
- **Sobrecarga de operadores**: El mismo patrón aplica a otros operadores, como `__sub__` para `-`, `__mul__` para `*` y `__eq__` para `==`, haciendo que las clases personalizadas se sientan como tipos nativos de Python.

---

## Ejercicio 25: Longitud del carrito usando sobrecarga de __len__

**Solución y explicación:**

```python
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)


cart = Cart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("mango")

print("Number of items in cart:", len(cart))
```

- **`self.items = []`**: Inicializa la lista interna que almacena el contenido del carrito. Cada instancia obtiene su propia lista independiente.
- **`__len__(self)`**: Python llama a esto automáticamente cuando se usa `len(cart)`. Delega en el `len()` incorporado sobre la lista interna, que ya sabe cómo contar sus elementos.
- **Diseño basado en protocolo**: Al implementar `__len__`, tu objeto `Cart` ahora participa en el protocolo de secuencias de Python. Esto también habilita verificaciones de veracidad: un objeto cuyo `__len__` retorna `0` se trata como `False` en un contexto booleano.
- **Métodos dunder relacionados**: Puedes extender este patrón con `__getitem__` para soportar indexado (por ejemplo, `cart[0]`) y con `__iter__` para soportar recorrer el carrito directamente.

---
