# Create a PokeBag class that can store multiple pokemons from different types. Add 5 pokemons to your PokeBag.
# There are 3 kind of pomenons:
# - Pikachu, who says “Pika-pika” and has 12 HP (health point)
# - Bubasaur, who says “Bulba-saur” and has 10 HP
# - Charmander, who says “Char-char” and has 10 HP
# Every pokemon has a random strength between 1 and 10.
# Pokemons can say their sound (see above) when their Speak method is called. The Speak method should return the pokemon’s sound.
# Create a function that returns the pokemon with the highest strength. In case of equal strengths, it’s your choice which one to return.
# 
# Example:
# pokeBag.add(Pikachu());
# pokeBag.add(Pikachu());
# pokeBag.add(Pikachu());
# pokeBag.add(Bulbasaur());
# pokeBag.add(Charmander());
# 
# print(pokeBag.get(0).speak());
# This should print Pika-pika
# 
# stongestPokemon = pokeBag.getStrongest();
# Should return the pokemon with the highest strength value

from random import randint


class PokeBag(object):
    
    def __init__(self):
        self.store = []
        self.pokemon = Pokemons()

    def add(self, pokemon):
        self.store.append(pokemon)
        
    def get(self):
        pass
    
    def get_strongest(self, pokemon_type, strength):
        strongest = self.store[0]
        for item in self.store[1:]:
            if item.strength > self.pokemon.strength:
                strongest = item
        return self.pokemon.to_string()
    
    def __str__(self):
        return self.get_strongest(self.pokemon.pokemon_type, self.pokemon.strength)


class Pokemons(object):
    
    def __init__(self):
        self.healthpoint = 0
        self.strength = randint(1,10)
        self.pokemon_type = "Pokemons"
    
    def to_string(self):
        return "{} : {} ".format(self.pokemon_type, self.strength)


class Pikachu(Pokemons):
    
    def __init__(self):
        super().__init__()
        self.healthpoint = 12
        self.pokemon_type = "Pikachu"
    def speak(self):
        return "Pika pika"


class Bulbasaur(Pokemons):
    
    def __init__(self):
        super().__init__()        
        self.healthpoint = 10
        self.pokemon_type = "Bulbasaur"

    def speak(self):
        return "Bulba-saur"


class Charmander(Pokemons):
    
    def __init__(self):
        super().__init__()        
        self.healthpoint = 10
        self.pokemon_type = "Bulbasaur"
        
    def speak(self):
        return "Char-char"


pokeBag = PokeBag()
pokeBag.add(Pikachu());
pokeBag.add(Pikachu());
pokeBag.add(Pikachu());
pokeBag.add(Bulbasaur());
pokeBag.add(Charmander());
print(pokeBag)
# print(pokeBag.get(0).speak());
# Should return the pokemon with the highest strength value

