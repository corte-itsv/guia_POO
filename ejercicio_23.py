class animal:
    pass

class dog(animal):
    pass

d = dog()

print("Is d an instance of Dog?", isinstance(d, dog))
print("Is d an instance of Animal?", isinstance(d, animal))
print("Is Dog a subclass of Animal?", isinstance(dog, animal))
print("Is Animal a subclass of Dog?", isinstance(animal, dog))
