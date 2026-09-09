# Pistas de Ejercicios de Programación Orientada a Objetos (OOP) en Python

## Ejercicio 1: Definir una clase Vehicle vacía

**Pista:**
- Usa la palabra clave `class` seguida del nombre de la clase y dos puntos.
- Usa `pass` dentro del cuerpo de la clase para que sea Python válido sin agregar atributos ni métodos.
- Después de definir la clase, puedes confirmar que existe imprimiendo `Vehicle` directamente.

## Ejercicio 2: Clase Vehicle con atributos de instancia

**Pista:**
- Define un método `__init__` que acepte `self`, `name`, `max_speed` y `mileage` como parámetros.
- Dentro de `__init__`, asigna cada parámetro a `self` para almacenarlos como atributos de instancia.
- Crea una instancia llamando a `Vehicle(...)` con los argumentos requeridos, y luego accede a los atributos usando notación de punto.

## Ejercicio 3: Clase Rectangle con área y perímetro

**Pista:**
- Almacena `length` y `width` como atributos de instancia dentro de `__init__`.
- Define `area(self)` que retorne `self.length * self.width`.
- Define `perimeter(self)` que retorne `2 * (self.length + self.width)`.

## Ejercicio 4: Clase Student con promedio de notas

**Pista:**
- Acepta `name` y `marks` (una lista) en el método `__init__` y asígnalos a `self`.
- En el método `average()`, usa `sum(self.marks) / len(self.marks)` para calcular la media.
- Usa `round()` si quieres controlar la cantidad de decimales en la salida.

## Ejercicio 5: Clase Product con calculadora de valor de stock

**Pista:**
- Define `__init__` con `name`, `price` y `quantity` como parámetros y asigna cada uno a `self`.
- En `total_value()`, retorna `self.price * self.quantity`.
- Usa un f-string con formato `:f.2` para mostrar el resultado como un valor monetario con dos decimales.

## Ejercicio 6: BankAccount con depósito y protección contra sobregiro

**Pista:**
- Inicializa `self.balance` en `__init__`.
- En `deposit()`, suma el monto directamente a `self.balance`.
- En `withdraw()`, usa una sentencia `if` para verificar si `amount <= self.balance` antes de descontar. Si no, imprime un mensaje de fondos insuficientes.

## Ejercicio 7: Clase Light con alternancia de estado encendido/apagado

**Pista:**
- Usa un atributo booleano como `self.is_on = False` en `__init__` para rastrear el estado actual.
- `turn_on()` debe establecer `self.is_on = True` e imprimir un mensaje de confirmación.
- `turn_off()` debe establecer `self.is_on = False` e imprimir un mensaje de confirmación.
- En `status()`, usa un condicional para imprimir `"ON"` u `"OFF"` según el valor de `self.is_on`.

## Ejercicio 8: Clase User con validación de contraseña

**Pista:**
- Almacena `username` y `password` como atributos de instancia en `__init__`.
- En `check_password(self, input_password)`, compara `input_password` con `self.password` usando `==` y retorna el resultado directamente.
- Llama al método con una contraseña correcta y luego con una incorrecta para verificar ambos resultados.

## Ejercicio 9: Clase Temperature con conversores de unidades

**Pista:**
- Almacena el valor en Celsius como `self.celsius` en `__init__`.
- Para Fahrenheit, usa la fórmula: `(celsius * 9/5) + 32`.
- Para Kelvin, usa la fórmula: `celsius + 273.15`.

## Ejercicio 10: Clase Notebook con agregado y visualización de notas

**Pista:**
- Inicializa `self.notes = []` dentro de `__init__` para que cada objeto `Notebook` comience con su propia lista vacía.
- En `add_note()`, usa `self.notes.append(note)` para agregar la nueva entrada.
- En `show_notes()`, usa `enumerate(self.notes, start=1)` para imprimir cada nota con un prefijo numerado.

## Ejercicio 11: CoffeeMachine con seguimiento de múltiples recursos

**Pista:**
- Almacena `water`, `coffee` y `milk` como atributos de instancia en `__init__`.
- En `make_latte()`, define las cantidades requeridas como variables locales y usa una sola condición `if` para verificar los tres recursos a la vez.
- Si la verificación se cumple, descuenta las cantidades requeridas de cada atributo e imprime los niveles restantes. En caso contrario, imprime un mensaje de fallo.

## Ejercicio 12: Atributo de clase compartido entre instancias

**Pista:**
- Define `color = "White"` directamente en el cuerpo de la clase, fuera de cualquier método, para convertirlo en un atributo de clase.
- Los atributos de instancia como `name` y `max_speed` se siguen definiendo en `__init__` como de costumbre.
- Para actualizar el atributo compartido en todas las instancias, reasígnalo mediante la clase misma: `Vehicle.color = "Red"`.

## Ejercicio 13: Subclase Bus que hereda de Vehicle

**Pista:**
- Para crear una clase hija, pasa la clase padre como argumento en la definición de la clase: `class Bus(Vehicle):`.
- Si la clase hija no agrega nada nuevo, usa `pass` en su cuerpo.
- Crea una instancia de `Bus` usando los mismos argumentos que `Vehicle` y llama a `display()` para confirmar que la herencia funciona.

## Ejercicio 14: Sobrescribir un método del padre usando super()

**Pista:**
- Define `seating_capacity(self, capacity)` en la clase `Vehicle` y haz que imprima un mensaje usando el argumento capacity.
- En la clase `Bus`, define un método con el mismo nombre pero sobrescríbelo para llamar a `super().seating_capacity(50)`, pasando el valor por defecto `50` directamente.
- Llama a `bus.seating_capacity()` sobre una instancia de `Bus` sin argumentos para confirmar que el valor por defecto se aplica.

## Ejercicio 15: Agregar tarifa de mantenimiento en clase hija vía super()

**Pista:**
- Define una clase `Vehicle` con un `__init__` que acepte `base_fare` y lo almacene como atributo de instancia.
- Crea una clase `Taxi` que herede de `Vehicle`.
- En `Taxi.__init__`, llama a `super().__init__(base_fare)` para inicializar al padre, y luego calcula la tarifa de mantenimiento como `base_fare * 0.10`.
- Agrega un método `total_fare()` que retorne `self.base_fare + self.maintenance_fee`.

## Ejercicio 16: Polimorfismo con speak() en Dog y Cat

**Pista:**
- Define una clase `Animal` con un método `speak()` que retorne una cadena genérica como `"Some sound"`.
- Crea las clases `Dog` y `Cat` que hereden de `Animal`.
- Sobrescribe `speak()` en cada subclase para retornar la cadena de sonido apropiada.
- Instancia ambas clases y llama a `speak()` en cada objeto para verificar la salida.

## Ejercicio 17: Lógica de pago para empleados de tiempo completo vs medio tiempo

**Pista:**
- Define una clase base `Employee` con `__init__` que acepte `name` y un método `calculate_pay()` que pueda dejarse como marcador de posición.
- En `FullTimeEmployee`, almacena el `salary` anual y calcula el pago mensual como `salary / 12`.
- En `PartTimeEmployee`, almacena `hourly_rate` y `hours_worked`, y luego calcula el pago como su producto.
- Sobrescribe `calculate_pay()` en cada subclase con la fórmula apropiada.

## Ejercicio 18: Subclases Shape con métodos area() personalizados

**Pista:**
- Define una clase base `Shape` con un método `area()` que retorne `0` como marcador de posición.
- Para `Circle`, usa la fórmula `3.14159 * radius ** 2`.
- Para `Square`, usa `side ** 2`.
- Para `Triangle`, usa `0.5 * base * height`.

## Ejercicio 19: Subclases Media con atributos específicos por tipo

**Pista:**
- Define una clase base `Media` con `title` y `price` en `__init__`.
- Cada subclase debe llamar a `super().__init__(title, price)` y luego agregar su propio atributo único: `author` para `Book`, `frequency` para `Magazine`, y `duration` para `DVD`.
- Sobrescribe un método `describe()` en cada subclase para imprimir una cadena formateada usando los atributos compartidos y únicos.

## Ejercicio 20: Subclase DiscountedOrder con 10% de descuento

**Pista:**
- Define una clase `Order` con atributos `order_id` y `total` y un método `get_total()` que retorne `self.total`.
- En `DiscountedOrder`, llama a `super().__init__(order_id, total)` y sobrescribe `get_total()` para retornar `self.total * 0.90`.
- Imprime tanto el `self.total` original como el resultado con descuento de `get_total()` para mostrar la diferencia.

## Ejercicio 21: Jerarquía de clases Vehicle con Bike, Truck y Bus

**Pista:**
- Define una clase base `Vehicle` con un atributo `max_speed` establecido en `0` y un método `describe()` que lo imprima.
- Crea las subclases `Bike`, `Truck` y `Bus`, cada una estableciendo su propio `max_speed` en `__init__`.
- Sobrescribe `describe()` en cada subclase, o confía en el método del padre si el formato de salida es el mismo.

## Ejercicio 22: Identificar la clase de un objeto usando type()

**Pista:**
- Define algunas clases simples (pueden tener cuerpos vacíos usando `pass`).
- Crea un objeto de cada clase.
- Usa `type(obj).__name__` para obtener el nombre de la clase como cadena, o compara `type(obj)` directamente con la clase misma (por ejemplo, `type(obj) == Dog`).

## Ejercicio 23: Verificación de tipos con isinstance() e issubclass()

**Pista:**
- Define una clase base `Animal` y una subclase `Dog` que herede de ella.
- Usa `isinstance(obj, ClassName)` para verificar si un objeto es instancia de una clase o de cualquiera de sus clases padre.
- Usa `issubclass(ChildClass, ParentClass)` para verificar si una clase hereda de otra.
- Ten en cuenta que `isinstance(d, Animal)` retorna `True` aunque `d` fue creado desde `Dog`, porque `Dog` hereda de `Animal`.

## Ejercicio 24: Suma de vectores usando sobrecarga de __add__

**Pista:**
- Define una clase `Vector` con atributos `x` e `y` en `__init__`.
- Implementa `__add__(self, other)` para retornar un nuevo `Vector` cuyo `x` sea `self.x + other.x` y cuyo `y` sea `self.y + other.y`.
- Implementa `__repr__` o `__str__` para controlar cómo se imprime el objeto.
- Pruébalo escribiendo `v1 + v2` e imprimiendo el resultado.

## Ejercicio 25: Longitud del carrito usando sobrecarga de __len__

**Pista:**
- Define una clase `Cart` con un `__init__` que inicialice una lista vacía `self.items = []`.
- Agrega un método `add_item(item)` que agregue elementos a `self.items`.
- Implementa `__len__(self)` para retornar `len(self.items)`.
- Una vez definido `__len__`, Python lo usará automáticamente cada vez que llames a `len(cart)` sobre tu objeto.
