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
        return sum(self.marks) / len(self.marks)


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
