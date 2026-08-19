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
- Usa un f-string con formato `:.2f` para mostrar el resultado como un valor monetario con dos decimales.

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
