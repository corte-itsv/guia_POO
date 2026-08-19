# Ejercicios de Programación Orientada a Objetos (OOP) en Python


## Ejercicio 1: Definir una clase Vehicle vacía

**Consigna:** Escribe un programa en Python para crear una clase llamada `Vehicle` que no tenga variables ni métodos definidos dentro.

**Propósito:** Este ejercicio introduce la forma más básica de definición de una clase en Python. Enseña la sintaxis necesaria para declarar una clase y el uso de la palabra clave `pass` como marcador de posición, algo esencial cuando se quiere definir una clase o función vacía sin provocar un error de sintaxis.

**Entrada dada:** No se requiere entrada.

**Salida esperada:** `<class '__main__.Vehicle'>`

**Pista:**
- Usa la palabra clave `class` seguida del nombre de la clase y dos puntos.
- Usa `pass` dentro del cuerpo de la clase para que sea Python válido sin agregar atributos ni métodos.
- Después de definir la clase, puedes confirmar que existe imprimiendo `Vehicle` directamente.


## Ejercicio 2: Clase Vehicle con atributos de instancia

**Consigna:** Escribe un programa en Python para crear una clase `Vehicle` con dos atributos de instancia: `max_speed` y `mileage`. Crea un objeto de la clase e imprime ambos atributos.

**Propósito:** Aprende a definir atributos de instancia usando el método constructor `__init__`. Los atributos de instancia son únicos para cada objeto, lo que significa que distintos objetos `Vehicle` pueden tener diferentes valores de velocidad y kilometraje. Este es un concepto fundamental en la programación orientada a objetos.

**Entrada dada:** `vehicle1 = Vehicle("Tesla Model S", 250, 18)`

**Salida esperada:** `Vehicle Name: Tesla Model S, Speed: 250, Mileage: 18`

**Pista:**
- Define un método `__init__` que acepte `self`, `name`, `max_speed` y `mileage` como parámetros.
- Dentro de `__init__`, asigna cada parámetro a `self` para almacenarlos como atributos de instancia.
- Crea una instancia llamando a `Vehicle(...)` con los argumentos requeridos, y luego accede a los atributos usando notación de punto.

## Ejercicio 3: Clase Rectangle con área y perímetro

**Consigna:** Escribe un programa en Python para crear una clase `Rectangle` con `length` y `width` como atributos de instancia, y dos métodos: `area()` que retorna el área y `perimeter()` que retorna el perímetro.

**Propósito:** Aprende a agregar métodos de instancia a una clase. Los métodos permiten que los objetos realicen operaciones usando sus propios datos, lo cual es un principio clave del encapsulamiento en OOP. Calcular propiedades geométricas es un contexto claro y práctico para entender cómo `self` conecta los métodos con los datos de la instancia.

**Entrada dada:** `rect = Rectangle(10, 4)`

**Salida esperada:** `Area = 40` y `Perimeter = 28`

**Pista:**
- Almacena `length` y `width` como atributos de instancia dentro de `__init__`.
- Define `area(self)` que retorne `self.length * self.width`.
- Define `perimeter(self)` que retorne `2 * (self.length + self.width)`.

## Ejercicio 4: Clase Student con promedio de notas

**Consigna:** Escribe un programa en Python para crear una clase `Student` que almacene el nombre (`name`) de un estudiante y una lista de notas (`marks`). Agrega un método `average()` que calcule y retorne el promedio de todas las notas.

**Propósito:** Este ejercicio muestra cómo los atributos de instancia pueden almacenar tipos de datos complejos, como listas, y no solo valores simples. También practica la combinación de OOP con operaciones de listas y aritmética, un patrón común en libros de calificaciones, paneles de control y herramientas de reportes.

**Entrada dada:** `s1 = Student("Alice", [85, 90, 78, 92, 88])`

**Salida esperada:** `Alice's Average Grade: 86.6`

**Pista:**
- Acepta `name` y `marks` (una lista) en el método `__init__` y asígnalos a `self`.
- En el método `average()`, usa `sum(self.marks) / len(self.marks)` para calcular la media.
- Usa `round()` si quieres controlar la cantidad de decimales en la salida.

## Ejercicio 5: Clase Product con calculadora de valor de stock

**Consigna:** Escribe un programa en Python para crear una clase `Product` con tres atributos de instancia: `name`, `price` y `quantity`. Agrega un método `total_value()` que retorne el valor total del stock multiplicando el precio por la cantidad.

**Propósito:** Este ejercicio modela un escenario de negocio real usando OOP. Refuerza cómo los métodos de instancia pueden derivar nueva información a partir de atributos existentes, un patrón muy usado en gestión de inventario, comercio electrónico y aplicaciones financieras.

**Entrada dada:** `p1 = Product("Laptop", 899.99, 5)`

**Salida esperada:** `Total stock value of Laptop: $4499.95`

**Pista:**
- Define `__init__` con `name`, `price` y `quantity` como parámetros y asigna cada uno a `self`.
- En `total_value()`, retorna `self.price * self.quantity`.
- Usa un f-string con formato `:.2f` para mostrar el resultado como un valor monetario con dos decimales.

## Ejercicio 6: BankAccount con depósito y protección contra sobregiro

**Consigna:** Escribe un programa en Python para crear una clase `BankAccount` con un atributo `balance` y dos métodos: `deposit(amount)` que agrega fondos al saldo, y `withdraw(amount)` que descuenta fondos pero evita que el saldo quede por debajo de cero.

**Propósito:** Aprende validación de datos y lógica condicional dentro de métodos de instancia. Evitar el sobregiro es una regla de negocio del mundo real, y al implementarla aquí aprendes cómo las clases pueden imponer restricciones sobre sus propios datos, una idea central detrás del encapsulamiento en OOP.

**Entrada dada:** Saldo inicial de `1000`, depósito de `500`, retiro de `200`, y luego un intento de retirar `2000`.

**Salida esperada:**

```
Balance after deposit: 1500
Balance after withdrawal: 1300
Insufficient funds. Current balance: 1300
```

**Pista:**
- Inicializa `self.balance` en `__init__`.
- En `deposit()`, suma el monto directamente a `self.balance`.
- En `withdraw()`, usa una sentencia `if` para verificar si `amount <= self.balance` antes de descontar. Si no, imprime un mensaje de fondos insuficientes.

## Ejercicio 7: Clase Light con alternancia de estado encendido/apagado

**Consigna:** Escribe un programa en Python para crear una clase `Light` con tres métodos: `turn_on()` que enciende la luz, `turn_off()` que la apaga, y `status()` que informa si la luz está actualmente encendida o apagada.

**Propósito:** Este ejercicio modela un objeto con estado simple, donde el objeto recuerda y cambia su propia condición a lo largo del tiempo. Introduce el concepto de gestión de estado dentro de una clase, un patrón presente en componentes de interfaz, dispositivos IoT, objetos de videojuegos y motores de flujo de trabajo.

**Entrada dada:** Crea un objeto `Light`, llama a `turn_on()`, verifica `status()`, llama a `turn_off()` y verifica `status()` nuevamente.

**Salida esperada:**

```
Light is ON
Current status: ON
Light is OFF
Current status: OFF
```

**Pista:**
- Usa un atributo booleano como `self.is_on = False` en `__init__` para rastrear el estado actual.
- `turn_on()` debe establecer `self.is_on = True` e imprimir un mensaje de confirmación.
- `turn_off()` debe establecer `self.is_on = False` e imprimir un mensaje de confirmación.
- En `status()`, usa un condicional para imprimir `"ON"` u `"OFF"` según el valor de `self.is_on`.

## Ejercicio 8: Clase User con validación de contraseña

**Consigna:** Escribe un programa en Python para crear una clase `User` que almacene un `username` y un `password`. Agrega un método `check_password(input_password)` que retorne `True` si la entrada coincide con la contraseña almacenada, y `False` en caso contrario.

**Propósito:** Este ejercicio introduce la idea de acceso controlado a datos sensibles dentro de una clase. En lugar de exponer la contraseña directamente, la clase ofrece un método dedicado para verificarla. Este patrón refleja un principio central del encapsulamiento en OOP, donde los datos internos están protegidos y solo se accede a ellos mediante interfaces definidas.

**Entrada dada:** `u1 = User("alice", "secure123")`

**Salida esperada:**

```
True  
False
```

**Pista:**
- Almacena `username` y `password` como atributos de instancia en `__init__`.
- En `check_password(self, input_password)`, compara `input_password` con `self.password` usando `==` y retorna el resultado directamente.
- Llama al método con una contraseña correcta y luego con una incorrecta para verificar ambos resultados.

## Ejercicio 9: Clase Temperature con conversores de unidades

**Consigna:** Escribe un programa en Python para crear una clase `Temperature` que almacene una temperatura en grados Celsius. Agrega dos métodos: `to_fahrenheit()` que convierte y retorna el valor en Fahrenheit, y `to_kelvin()` que convierte y retorna el valor en Kelvin.

**Propósito:** Este ejercicio demuestra cómo una clase puede actuar como contenedor de datos con lógica de conversión incorporada. Refuerza la escritura de múltiples métodos que operan sobre el mismo atributo de instancia, y aplica fórmulas matemáticas sencillas en un contexto científico práctico.

**Entrada dada:** `t = Temperature(100)`

**Salida esperada:**

```
Celsius: 100
Fahrenheit: 212.0
Kelvin: 373.15
```

**Pista:**
- Almacena el valor en Celsius como `self.celsius` en `__init__`.
- Para Fahrenheit, usa la fórmula: `(celsius * 9/5) + 32`.
- Para Kelvin, usa la fórmula: `celsius + 273.15`.

## Ejercicio 10: Clase Notebook con agregado y visualización de notas

**Consigna:** Escribe un programa en Python para crear una clase `Notebook` que mantenga una lista interna de notas. Agrega un método `add_note(note)` que agregue una nueva nota a la lista, y un método `show_notes()` que imprima todas las notas almacenadas.

**Propósito:** Este ejercicio muestra cómo una clase puede gestionar una colección de datos que crece a lo largo de su vida útil. Practica la inicialización de una estructura de datos mutable dentro de `__init__` y la escritura de métodos que tanto modifican como leen esa estructura, un patrón que aparece en listas de tareas, colas de mensajes, registros y muchas otras aplicaciones.

**Entrada dada:** Agregar tres notas: `"Buy groceries"`, `"Read a book"`, `"Call the doctor"`.

**Salida esperada:**

```
1. Buy groceries
2. Read a book
3. Call the doctor
```

**Pista:**
- Inicializa `self.notes = []` dentro de `__init__` para que cada objeto `Notebook` comience con su propia lista vacía.
- En `add_note()`, usa `self.notes.append(note)` para agregar la nueva entrada.
- En `show_notes()`, usa `enumerate(self.notes, start=1)` para imprimir cada nota con un prefijo numerado.

## Ejercicio 11: CoffeeMachine con seguimiento de múltiples recursos

**Consigna:** Escribe un programa en Python para crear una clase `CoffeeMachine` que rastree tres atributos de recursos: `water`, `coffee` y `milk` (en ml/g). Agrega un método `make_latte()` que verifique si hay recursos suficientes disponibles, los descuente si es así, e imprima un mensaje apropiado en cualquiera de los casos.

**Propósito:** Este ejercicio combina gestión de estado, seguimiento de recursos y lógica condicional dentro de una sola clase. Refleja cómo los sistemas con estado del mundo real (máquinas expendedoras, sistemas de inventario, gestores de recursos de videojuegos) verifican condiciones previas antes de ejecutar una acción y actualizan su estado interno solo cuando la acción es válida.

**Entrada dada:** `CoffeeMachine(water=300, coffee=100, milk=200)`. Un latte requiere `200ml` de agua, `20g` de café y `150ml` de leche.

**Salida esperada:**

```
Latte made! Remaining - Water: 100ml, Coffee: 80g, Milk: 50ml
Not enough resources to make a latte.
```

**Pista:**
- Almacena `water`, `coffee` y `milk` como atributos de instancia en `__init__`.
- En `make_latte()`, define las cantidades requeridas como variables locales y usa una sola condición `if` para verificar los tres recursos a la vez.
- Si la verificación se cumple, descuenta las cantidades requeridas de cada atributo e imprime los niveles restantes. En caso contrario, imprime un mensaje de fallo.
