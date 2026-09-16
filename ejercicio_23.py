
class animal:
    pass

class dog(animal):
    pass


d = dog()

print(f'es d una instancia de dog? {isinstance(d, dog)}')
print(f'es d una instancia de animal? {isinstance(d, animal)}')
print(f'es dog una subclase de animal? {issubclass(dog, animal)}')
print(f'es animal una subclase de dog? {issubclass(animal, dog)}')